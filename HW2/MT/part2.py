#!   /usr/bin/python

import urllib
from bs4 import BeautifulSoup
from datetime import datetime
import md5

n = datetime.now();
links = [];
cnt = 0; 

f = open("mement", "w")

for link in open("valids", "r"):
	head = "http://mementoweb.org/timemap/link/";
	resp = urllib.urlopen(head+link);

	html = resp.read();
	html = html.split("\n")

	cnt = 0;
	for line in html:
		if "datetime" in line:
			cnt = cnt + 1;
			# ind = line.find("datetime")
			# m = line[ind+15:len(line)-5];
			# print m
			# f.write(str((n - datetime.strptime(m, "%d %b %Y %H:%M:%S")).days)+"\n") 
	# print cnt, link	
	f.write(str(cnt)+", "+str(link))	

f.close();