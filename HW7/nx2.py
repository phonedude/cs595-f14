#! /usr/bin/python


import json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import igraph

g = igraph.read("weighted_karate.gml")
h = g.community_leading_eigenvector(clusters=2)
[a,b] = h.subgraphs();

igraph.write(a, "a", format="gml");
igraph.write(b, "b", format="gml");

c = nx.read_gml("a");
data = json_graph.node_link_data(c);
with open('c.json', 'w') as f:
 json.dump(data, f, indent=4);


d = nx.read_gml("b");
data = json_graph.node_link_data(d);
with open('d.json', 'w') as f:
 json.dump(data, f, indent=4);
#with open('rgraph.json', 'w') as f:
#    json.dump(data, f, indent=4)
