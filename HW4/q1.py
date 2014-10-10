#! /usr/bin/python

import urllib2 as ul
from bs4 import BeautifulSoup as bs
import re

def getLinks(url):
 try:
  req = ul.Request(url);
  res = ul.urlopen(req);
  html = res.read();
  soup = bs(html);
  links = []
  for lks in soup.find_all('a'):
   temp = lks.get('href');
   #print temp[0:4]
   if ("http" == (temp[0:4])):
    g.write(temp+"\n");
    #h.write(line+" -> "+temp+"\n");
 except:
  print "ERROR: "+url+"\n"
  pass;

f = open("100","r");
#h = open("graph", "w");

#h.write("diagraph test {\n");
cnt = 0; 
for line in f:
 cnt = cnt +1
 print cnt;

 g = open("./lks/"+"{0:0>3}".format(str(cnt)),"w+");
 g.write("site: \n"+str(line)+"links: \n");
 #print line;
 getLinks(line);

#h.write("}"); 
