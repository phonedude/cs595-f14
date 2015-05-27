#! /usr/bin/env python 

import networkx as nx

G = nx.karate_club_graph()
print "Node Degree"
for v in G:
	#print v, G.degree(v)

print nx.betweenness_centrality(G)
