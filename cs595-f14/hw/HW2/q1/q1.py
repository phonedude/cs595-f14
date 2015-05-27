#! /usr/bin/python

# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
from pprint import pprint
import urllib2
import httplib2

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
	for rs in r.json():
		temp = rs.get('entities').get('urls');
		num =  rs.get('id');
		# check if there were urls in tweet
		if len(temp) != 0:		
			num =  rs.get('id');
			temp = str((temp[0])['url']);
			# attempt to get the 
			try:
				h = httplib2.Http(".cache_httplib")
				h.follow_all_redirects = True
				h.force_exception_to_status_code = True
				resp = h.request(temp, "GET")[0]
				if resp['status'] == '200':
					# this is the final redirected url
					print resp['content-location']
					links.append(resp['content-location'])
			except:
				pass
	return num, links

if __name__ == "__main__":
		if not OAUTH_TOKEN:
				token, secret = setup_oauth()
				print "OAUTH_TOKEN: " + token
				print "OAUTH_TOKEN_SECRET: " + secret
				print
		else:
				oauth = get_oauth()

				# initial variables
				numURLs = 1000;
				site = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="
				name = "timoreilly"
				cnt  = "&count=20"
				filt = "&filter%3Alinks"
				uniqs = [];
				things = [];
				# initial request with count
				r = requests.get(url=site+name+cnt+filt, auth=oauth)
				[num, temp] = getURL(r)

				for i in temp:
					things.append(i)

				while len(uniqs) < numURLs:
					# request with max id
					max_id = "&max_id="+str(num-1)
					r = requests.get(url=site+name+cnt+max_id+filt, auth=oauth)
					[num, temp] = getURL(r)
					# tack those onto the end
					for i in temp:
						things.append(i)

					# get the unique ones	
					uniqs = set(things)
						
				for i in uniqs:
					print i;

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
		

