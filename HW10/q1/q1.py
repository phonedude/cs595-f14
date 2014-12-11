#! /usr/bin/python 
import feedparser
import feedfilter
import docclass
import random
import re
cl=docclass.fisherclassifier(docclass.getwords)
cl.setdb('soccerphile.db')

feed = "feed.xml"
f=feedparser.parse(feed)
g = open("class.txt","r")
next(g)
cat = [] 
for line in g:
	tmp = line.split(' ')[1].strip('\n')
	cat.append(tmp)

num = 50

def q1Train(f,cat,num,classifier):
  # Get feed entries and loop over them
  print "--- TRAINING  ---"
  for entry in f['entries']:
  	i = f.entries.index(entry)
  	if( i < num):
	    print
	    print '-----'
	    print 'Title:     '+entry['title'].encode('utf-8')
	    fulltext='%s\n%s' % (entry['title'],entry['summary'][0])
	    print i
    	classifier.train(fulltext, cat[i])

  for i in classifier.categories():
   	classifier.setminimum(i,.16)

def q1Test(f,cat,num,classifier):
  print "--- TESTING  ---"
  h = open("table.txt", "w")
  h.write("title, string, cprob, pred, act\n")

  for entry in f['entries']:
  	i = f.entries.index(entry)
  	if( i >= num):
	    print
	    print '-----'
	    print 'Title:     '+entry['title'].encode('utf-8')
	    fulltext='%s\n%s' % (entry['title'],entry['summary'])
	    print i
	    a = feedfilter.entryfeatures(entry)
	    b = random.randint(0,len(a)-1)
	    c = ' '.join(a)
	    #print a
	    fulltext='%s\n%s' % (entry['title'],entry['summary'][0])
	    # cls = classifier.classify(a.items()[b][0])
	    # cls = classifier.classify(fulltext)
	    cls = classifier.classify(fulltext)

	    f.entries[i].pred = cls
	    f.entries[i].cls = cat[i]
	    # cls=raw_input('Enter category: ')
	    # cprob = classifier.fisherprob(entry['title'], cls)
	    cprob = classifier.fisherprob(a.items()[b][0], cls)
	    cprob = classifier.fisherprob(c, cls)
	    print "Guess: "+str(cls)
	    print "Actual: "+str(cat[i])
	    print "C Prob: "+str(cprob)

	    fout = '%s, %s, %f, %s, %s\n' % (re.sub(r'[^\x00-\x7F]+', '', entry['title'][0:30]), a.items()[b][0], cprob, cls, cat[i])
	    h.write(fout)
def fmeasure(f, num):
	tp, fp, fn = 0, 0, 0
	for i in range(num, 100):
		if(f.entries[i].pred == f.entries[i].cls):
			tp +=1
		if(f.entries[i].pred != f.entries[i].cls):
			fp +=1
		if(not f.entries[i].pred):
			fn +=1

	prec = float(tp)/(tp + fp)
	recl = float(tp)/(tp +fn)

	fmeasure = 2*(prec*recl)/(prec+recl)
	print prec, recl
	print fmeasure

q1Train(f, cat, num, cl)
q1Test(f, cat, num, cl)
fmeasure(f,num)
