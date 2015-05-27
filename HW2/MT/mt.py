#!   /usr/bin/python

from urlparse import urlparse
from threading import Thread
import httplib, sys, urllib
from Queue import Queue

concurrent = 200

def doWork():
    while True:
        url = q.get()
        status, url = getStatus(url)
        doSomethingWithResult(status, url)
        q.task_done()

def getStatus(ourl):
    try:
        # url = urlparse(ourl)
        # conn = httplib.HTTPConnection(url.netloc)   
        # conn.request("HEAD", url.path)
        # res = conn.getresponse()
        resp = urllib.urlopen(ourl);
        # return res.status, ourl
        return resp.getcode(), resp.url
    except:
        return "error", ourl

def doSomethingWithResult(status, url):
    # print status, url
    if str(status) == '200':
        print "yay"
        links.append(url)

links = [];

f = open("valids", "w")
q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    for url in open('myfile3'):
        q.put(url.strip())
    q.join()
except KeyboardInterrupt:
    sys.exit(1)

print len(links)
for i in links:
    f.write(i+"\n")