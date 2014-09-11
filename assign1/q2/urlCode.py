#! /usr/bin/python
from bs4 import BeautifulSoup
import bs4
import urllib
import urllib2
import sys
import re
import time
from datetime import datetime

def oops(): 
 print "Didnt find it";
 exit()

print "URI program"
team = sys.argv[1];
sec = float(sys.argv[2]);
site = sys.argv[3];

while(1):
 # fetching the page from the internet
 request = urllib2.Request(site);
 file = urllib2.urlopen(request);
 # getting the soup from the html	
 html = file.read();
 soup = BeautifulSoup(html);

 team1 = [];
 reverse = 0;
 # check the away tsd first
 tds = soup.find_all("td", "away");
 for td in tds:	
  for kids in td.children:
   if isinstance(kids, bs4.element.Tag):
    for kid in kids.children:
     if isinstance(kid, bs4.element.Tag) and kid.string == team:
      there = kid;
      team1 = there.string;
 # the team was found in aways
 if team1 != []:
  # get parent tag
  away = there.parent.parent
  # hop over to score
  score =  away.next_sibling.next_sibling
  # weird cntr to store values in list
  cnt = 0
  for kids in score.h4.a.children:
   if isinstance(kids, bs4.element.Tag):
    score[cnt] = kids.string
    cnt = cnt +1;
  # hop over to home 
  home = score.next_sibling.next_sibling;
  for kids in home.children:
   if isinstance(kids, bs4.element.Tag):
    for kid in kids.children: 
     if isinstance(kid, bs4.element.Tag) and kid.string != None:
      team2 = kid.string;
 
 # check for team in home
 else:
  reverse = 1
  tds = soup.find_all("td", "home");
  for td in tds:
   for kids in td.children:
    if isinstance(kids, bs4.element.Tag):
     for kid in kids.children:
      if isinstance(kid, bs4.element.Tag) and kid.string == team:
       there = kid;
       team1 = there.string;
  if team1 == []:
   oops();
  else:
   home = there.parent.parent
   score = home.previous_sibling.previous_sibling;
   cnt = 1;
   for kids in score.h4.a.children:
    if isinstance(kids, bs4.element.Tag):
     score[cnt] = kids.string;
     cnt = cnt - 1; 
   away = score.previous_sibling.previous_sibling;
   for kids in away.children:
    if isinstance(kids, bs4.element.Tag):
     for kid in kids.children:
      if isinstance(kid, bs4.element.Tag) and kid.string != None:
       team2 = kid.string;
 if team1 != [] and team !=[]:
  if reverse == 0:
   print team1, score[0],"-", score[1], team2,"\t", datetime.now().strftime('%H:%M:%S')
  elif reverse == 1:
   print team2, score[1],"-", score[0], team1, "\t", datetime.now().strftime('%H:%M:%S')
  else: 
   print "Something went wrong"
 else: 
                                     print "Sorry cant find that team. check your spelling";i

 time.sleep(sec);
