#! /usr/bin/python

# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
from pprint import pprint
import urllib2
import httplib2
import time

from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue
import httplib2
import urllib2

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"
CONSUMER_KEY = "fZJV8AbOSPvE3RbELyok0vjfa"
CONSUMER_SECRET = "HmjPCwt5ysI51pYtCGbmQKJU5IqUtIqI8sL2fGpvKhMIYFHaq6"
OAUTH_TOKEN = "2822206502-dN9QiytMOBKSRrirhmzGYHLcGypaGMoa9X3vZvv"
OAUTH_TOKEN_SECRET = "cR0B9TgqWaKGOOh0eGsG8lEFi1BtQvKczlTGXBEggqAaO"

def setup_oauth():
		"""Authorize your app via identifier."""
		# Request token
		oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
		r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
		credentials = parse_qs(r.content)
		resource_owner_key = credentials.get('oauth_token')[0]
		resource_owner_secret = credentials.get('oauth_token_secret')[0]
		# Authorize
		authorize_url = AUTHORIZE_URL + resource_owner_key
		print 'Please go here and authorize: ' + authorize_url
		verifier = raw_input('Please input the verifier: ')
		oauth = OAuth1(CONSUMER_KEY,
									 client_secret=CONSUMER_SECRET,
									 resource_owner_key=resource_owner_key,
									 resource_owner_secret=resource_owner_secret,
									 verifier=verifier)
		# Finally, Obtain the Access Token
		r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
		credentials = parse_qs(r.content)
		token = credentials.get('oauth_token')[0]
		secret = credentials.get('oauth_token_secret')[0]
		return token, secret

def get_oauth():
		oauth = OAuth1(CONSUMER_KEY,
								client_secret=CONSUMER_SECRET,
								resource_owner_key=OAUTH_TOKEN,
								resource_owner_secret=OAUTH_TOKEN_SECRET)
		return oauth 

# returns id num and list of links
def getURL(r):
	links = [];
	# traverse json object of multiple tweets
	cnt = 0;
	for rs in r.json():
		cnt = cnt +1;
		temp = rs.get('entities').get('urls');
		num =  rs.get('id');
		# check if there were urls in tweet
		if len(temp) != 0:		
			num =  rs.get('id');
			temp = str((temp[0])['url']);
			# try:
			# 	q.put(temp.strip())
			# print temp
			things.append(temp)
			# attempt to get the 
			# try:
			# 	h = httplib2.Http(".cache_httplib")
			# 	h.follow_all_redirects = True
			# 	h.force_exception_to_status_code = True
			# 	resp = h.request(temp, "GET")[0]
			# 	if resp['status'] == '200':
			# 		# this is the final redirected url
			# 		print resp['content-location']
			# 		links.append(resp['content-location'])
			# except:
			# 	pass
			
			# except KeyboardInterrupt:
			# 	sys.exit(1)
	q.join()
	time.sleep(1)			
	print "REQUEST COMPLETE: "+str(len(things));
	return num, links

concurrent = 100
def doWork():
    while True:
        url = q.get()
        status, url = getStatus(url)
        if status == '200':
        	print url 
        	# g.write(url+"\n");
        	links.append(url)
        q.task_done()

def getStatus(ourl):
    try:
        # resp = urllib2.urlopen(ourl)
        h = httplib2.Http(".cache_httplib")
        h.follow_all_redirects = True
        h.force_exception_to_status_code = True
        resp = h.request(ourl, "HEAD")[0]
        # url = urlparse(ourl)
        # conn = httplib.HTTPConnection(url.netloc)   
        # conn.request("HEAD", url.path)
        # res = conn.getresponse()
        return  resp['status'], resp['content-location']
        
    except:
        return "error", ourl



if __name__ == "__main__":
		if not OAUTH_TOKEN:
				token, secret = setup_oauth()
				print "OAUTH_TOKEN: " + token
				print "OAUTH_TOKEN_SECRET: " + secret
				print
		else:
				oauth = get_oauth()

				# initial variables
				numURLs = 2000;
				site = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="
				names = ["timoreilly"]; #, "AP", "realjohngreen","cnnbrk"]; #,   "raganwald"] #, "StephenAtHome", "pimpsofjoytime"];
				cnt  = "&count=200"
				filt = "&filter%3Alinks"
				uniqs = [];
				things = [];

				links = [];

				q = Queue(concurrent * 2)
				for i in range(concurrent):
				    t = Thread(target=doWork)
				    t.daemon = True
				    t.start()

				
				for name in names:
					# if len(things) < numURLs:    
						print name    
						# initial request with count
						r = requests.get(url=site+name+cnt+filt, auth=oauth)
						print r
						[num, temp] = getURL(r)

						for i in temp:
							things.append(i)

						# while len(things) < numURLs:
						for i in range(1,14):
							# request with max id
							# print len(things)
							max_id = "&max_id="+str(num-1)
							r = requests.get(url=site+name+cnt+max_id+filt, auth=oauth)
							[num, temp] = getURL(r)
							# tack those onto the end
							for i in temp:
								things.append(i)

						time.sleep(3);			
				# get the unique ones	
				uniqs = set(things)
				print len(uniqs)
				f = open('myfile3','w')	
				# g = open('urls3', 'w')
				for i in uniqs:
					f.write(i+"\n");

				# try:
				# 	for i in uniqs:
				# 		q.put(i.strip())	
				# 	q.join();			
				# except KeyboardInterrupt:
				# 	sys.exit(1)				

				# print len(links)
				# for i in links:
				# 	g.write(i+"\n");


				f.close();
				# g.close();
				

###############################################################################
###############################################################################
##	ORIGINAL DIRTY-WAY-OF-DOING-THINGS CODE
###############################################################################
###############################################################################
		# 		things = [];        
		# 		more_things = [];
		# 		num = 0;
		# 		while(len(things) < 5):			
		# 				if len(things) != 0:
		# 					max_id = "&max_id="+str(num-1)
		# 					r = requests.get(url=site+name+cnt+max_id, auth=oauth)
		# 				for rs in r.json():
		# 						num =  rs.get('id');
		# 						i = rs.get('entities').get('urls')
		# 						if len(i) != 0:
		# 								i = i[0]
		# 								temp = i['url'];
		# 								# print temp;
		# 								try:    
		# 										h = httplib2.Http(".cache_httplib")
		# 										h.follow_all_redirects = True
		# 										h.force_exception_to_status_code = True
		# 										resp = h.request(temp, "GET")[0]
		# 										if resp['status'] == '200':
		# 												loc = resp['content-location']
		# 												more_things.append(loc);
		# 												if not(loc in things):
		# 														things.append(loc);
		# 										elif resp['status'] == '200':
		# 												loc = resp['location']
		# 												more_things.append(loc);
		# 												if not(loc in things):
		# 														things.append(loc);
		# 										else: 
		# 												loc = resp['status'];
		# 										#req = urllib2.Request(temp, headers=hdr)   
		# 										#res = urllib2.urlopen(req);
		# 										#print  loc									
		# 								except ValueError:
		# 										pass;
		# 						#pprint(rs)
		# print len(more_things), len(things)
		# for thing in things:
		# 		print thing;
		

