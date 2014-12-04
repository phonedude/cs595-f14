#! /usr/bin/python 
import urllib2
from bs4 import BeautifulSoup as bs

# GET A REQUIRED NELSON BLOGS   # RETURNS TITLE AND FEED PAGE LIST
def getBlogInfoInit():
  Blogs = ["http://f-measure.blogspot.com/",
							"http://ws-dl.blogspot.com/"]
  ttl = []; feedLinks = []
  for nextBlog in Blogs:
		temp = []
		try:
			html = urllib2.urlopen(nextBlog).read()
			soup = bs(html)
			ttl.append(soup.title.string.encode('ascii'))
			rss = soup.find('link', type='application/atom+xml')
			if(rss != []):
				rss = rss.get('href')
				temp  = allPages(rss)
				temp.insert(0,rss)
				feedLinks.append(temp)
		except:
			pass	
  return ttl, feedLinks
# GET A RANDOM BLOG, EXTRACT TITLE AND FEED PAGES # RETURNS TITLE AND FEED PAGE LIST
def getBlogInfo():
	nextBlog = "https://www.blogger.com/next-blog?navBar=true&blogID=8145271598519191285"
	feedLinks = []
	try:
		resp = urllib2.urlopen(nextBlog)
		if (resp.code == 200):
			html = resp.read()
			soup = bs(html)
			ttl = soup.title.string.encode('ascii')
			rss = soup.find('link', type='application/atom+xml')
			if(rss != []):
				rss = rss.get('href')
				feedLinks = allPages(rss)
				feedLinks.insert(0,rss)
				return ttl, feedLinks
			else: 
				return ttl, rss
		else:
			return [], []
	except:
		return [], []
# COLLECTS ALL FEED PAGES # RETURNS LIST OF FEED PAGES
def allPages(link):
	pages = []
	tmp = nextPage(link)
	while(tmp != False):	
		pages.append(tmp)
		tmp = nextPage(tmp)
	return pages		
# CHECK FOR NEXT FEED PAGE # RETURN NEXT FEED PAGE OR FALSE
def nextPage(link):
	try:
		html = urllib2.urlopen(link).read()
		soup = bs(html)
		nxt = soup.find('link', rel="next")
		if(nxt != []):
			nxt = nxt.get('href')
			return nxt
	except:
		return False
def main():
	f = open("feedlist.txt", "w")
	g = open("feedstats.txt", "w")
	g.write("Title , Pages\n")
	titles = []; pageCnt = 0; links = []
	ttl, lks = getBlogInfoInit()
	for i in range(len(ttl)):
		titles.append(ttl[i])
		links.extend(lks[i])
		print "\""+ttl[i].lstrip().rstrip()+"\"", len(lks[i])
		g.write("\""+ttl[i].rstrip().lstrip()+"\" , "+str(len(lks[i]))+"\n");
	while(len(set(titles)) < 120):
		ttl, lks = getBlogInfo()
		if(ttl != []):
			titles.append(ttl)
			print "\""+ttl.lstrip().rstrip()+"\"", len(lks)
			g.write("\""+ttl.rstrip().lstrip()+"\" , "+str(len(lks))+"\n");
			links.extend(lks)
	for i in links:
		f.write(i+"\n")