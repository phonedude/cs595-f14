#! /usr/bin/python

# script that imports graph data and finds the strongly connected groups

from collections import defaultdict
import numpy as np
from scipy.sparse import csgraph


print "Graph Script\n"
f = open("graph.txt", 'r');
graph = defaultdict(list); 
array = np.zeros((14,14))

for line in f:
 line = line.replace(" ", "");
 print line
 line = line.replace("-->","");
 key = line[0];
 value = line[1];
 i = ord(key) - ord('A');
 j = ord(value) - ord('A') 
 array[i][j] = 1;
 graph[key].append(value);
f.close();

graph = sorted(graph.items())
comp, comp_list =  csgraph.connected_components(array, True, "strong")
a =  [list((np.where(comp_list == i))) for i in range(comp)]

final = [];
for i in range(len(a)):
  b =  (a[i][0].tolist());
  out = []
  for j in range(len(b)):
    out.append( chr(b[j] + ord('A')))
  final.append(out)

print "The strongly connected groups are:" 
print final


