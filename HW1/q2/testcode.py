#! /usr/bin/python
from bs4 import BeautifulSoup
import bs4
import urllib
import urllib2
import sys
import re

print "URI program"

#uni1 = sys.argv[1]; 
#uni2 = sys.argv[2];
#site = sys.argv[3];

#print uni1, uni2, site
team = "Old Dominion Univerisity";

url = "http://sports.yahoo.com/college-football/scoreboard/?week=2&conf=all";

request = urllib2.Request(url);
file = urllib2.urlopen(request);

html = file.read();

f = open("out.htm", 'w');
f.write(html)
soup = BeautifulSoup(html)


td = soup.find("td", "away");

for kids in td.children:
 if isinstance(kids, bs4.element.Tag):
  #print kids
  for kid in kids.children:
   if isinstance(kid, bs4.element.Tag) and kid.string != None:
    print kid.string
  
td = soup.find("td", "home");

for kids in td.children:
 if isinstance(kids, bs4.element.Tag):
  for kid in kids.children:
   if isinstance(kid, bs4.element.Tag) and kid.string != None:
    print kid.string

sc = soup.find("td", "score")

for i in sc.h4.a.children:
 print i.string

