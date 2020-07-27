import networkx as nx
nodes = [0,1,2,3,4]
edges = [(1,0),(0,2),(1,2),(1,3),(2,3),(0,4)]
G=nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
print(list(nx.all_simple_paths(G,0,1,cutoff=4)))
print(nx.has_path(G,0,3))

#{0: {1: {}, 2: {}, 4: {}}, 1: {0: {}, 2: {}, 3: {}}, 2: {0: {}, 1: {}, 3: {}}, 3: {1: {}, 2: {}}, 4: {0: {}}}
#visited = collections.OrderedDict.fromkeys([source])