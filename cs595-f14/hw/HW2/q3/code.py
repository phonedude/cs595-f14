#! /usr/bin/python

import json
from StringIO import StringIO
from datetime import datetime

n = datetime.now();
a = open("cdate","r");
b = a.read();
b = StringIO(b);
c = json.load(b);
m = c.get("Estimated Creation Date"); 

print datetime.strptime(m, "%Y-%m-%dT%H:%M:%S") - n ; 
#print datetime.strptime(c.get("Estimated Creation Date"),  - n

