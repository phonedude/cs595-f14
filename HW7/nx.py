#! /usr/bin/python


import json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph

g = nx.read_gml("weighted_karate.gml")

data = json_graph.node_link_data(g)
with open('wgraph.json', 'w') as f:
    json.dump(data, f, indent=4)
