#! /usr/bin/python

import json
from StringIO import StringIO
from datetime import datetime
import sys;

data = sys.stdin.read();

n = datetime.now();
a = data
b = a;
b = StringIO(b);
c = json.load(b);
m = c.get("Estimated Creation Date"); 

print (n - datetime.strptime(m, "%Y-%m-%dT%H:%M:%S")).days; 
#print datetime.strptime(c.get("Estimated Creation Date"),  - n

