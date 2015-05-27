import networkx as nx


def girvan_newman (G, print_biggest = False):
    """
    A very simple no bells and whistles implementation of
    girvan-newman, relying on networkx.

    Sicne this destroys the graph, it would be wise to make a copy of the graph
    at the top level, using::

       G.copy()
    """

    if len(G.nodes()) == 1:
        return [G.nodes()]
        
    def find_best_edge(G0):
        """
        Networkx implementation of edge_betweenness
        returns a dictionary. Make this into a list,
        sort it and return the edge with hoghest betweenness.
        """
        eb = nx.edge_betweenness_centrality(G0)
        eb_il = eb.items()
        eb_il.sort(key=lambda x: x[1], reverse=True)
        return eb_il[0][0]

    components = nx.connected_component_subgraphs(G)
    
    while  len(list(components)) == 1:
        G.remove_edge(*find_best_edge(G))
        components = nx.connected_component_subgraphs(G)

    res = [c.nodes() for c in components]
    if print_biggest:
        for c in res:
            print c
    for c in components:
        res.extend(girvan_newman(c))
    return res
    

#if __name__ == '__main__':

    #kn = nx.read_gml('karate.gml')
    #components = girvan_newman(kn, print_biggest=True)
    
            
