#!/usr/bin/python
# -*- coding: utf-8 -*-
import feedparser
import re
import pickle

from math import log

def getwordcounts(url):
    '''
    Returns title and dictionary of word counts for an RSS feed
    '''
    # Parse the feed
    d = feedparser.parse(url)
    wc = {}

    # Loop over all the entries
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary

        else:
            summary = e.description

        # Extract a list of words
        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1

    return (d.feed.title, wc)


def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']

def main():
    apcount = {}
    wordcounts = {}
    feedlist = [line for line in file("feedlist.txt")]
    for feedurl in feedlist:
        try:
            (title, wc) = getwordcounts(feedurl)
            wordcounts[title] = wc
            for (word, count) in wc.items():
                apcount.setdefault(word, 0)
                if count >= 1:
                    apcount[word] += 1
        except:
            print 'Failed to parse feed %s' % feedurl

    

    # Rows in the term matrix must be divided by their length
    # Rows must be added based on term
    # this is the sum of all term frequencies
    tf = {}
    blogs = wordcounts
    # go through every blog
    for blog in blogs:
        # go through every term
        for term in blogs[blog]:
            if term in tf: 
                tf[term] += blogs[blog][term]/float(len(blogs[blog])) 
            else:
                tf[term] = blogs[blog][term]/float(len(blogs[blog])) 


    corp = float(len(blogs))
    idf = {}
    for i in apcount:
        idf[i] = log(corp/apcount[i])/log(2)

    tfidf = {}
    for i in tf:
        tfidf[i] = tf[i]*idf[i]

    

    new = []
    for i in tfidf:
        new.append((i, tfidf[i]))

    new.sort(key=lambda tup:tup[1], reverse=True)

    wordlist = []
    for i in range(500):
        print new[i][0]
        wordlist.append(new[i][0].encode('ascii'))

    pickle.dump(apcount, open( "ap.p", "wb" ) )
    pickle.dump(wordcounts, open( "wrd.p", "wb" ) )
    


    # ##
    # wordrank = []
    # for (w, bc) in apcount.items():
    #     #frac = float(bc) / len(feedlist)
    #     #if frac > 0.1 and frac < 0.5:
    #     wordrank.append((w,bc))
    # #print wordrank
    # 
    # # sort list based on frequency
    # wordrank.sort(key=lambda tup:tup[1], reverse=True)
    # for i in range(len(wordrank)):
    #     print wordrank[i][0]
    #     wordlist.append(wordrank[i][0].encode('ascii'))
    # ##



    out = file('blogdata2.txt', 'w')
    out.write('Blog')
    for word in wordlist:
        out.write('\t%s' % word)
    out.write('\n')
    for (blog, wc) in wordcounts.items():
        print blog
        out.write(blog)
        for word in wordlist:
            if word in wc:
                out.write('\t%d' % wc[word])
            else:
                out.write('\t0')
        out.write('\n')
