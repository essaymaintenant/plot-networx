import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import re # Regular Expressions
import networkx as nx # for network diagrams

# adaptations/variations on other authors' code:

G = nx.Graph()
G.add_edge(1,2,color='r',weight=2)
G.add_edge(2,3,color='b',weight=4)
G.add_edge(3,4,color='g',weight=6)

pos = nx.circular_layout(G)

edges = G.edges()
G.nodes()

nx.set_node_attributes(G,'color','r')
nodecols = nx.get_node_attributes(G,'color').values()   # get result as DICTIONARY
# colors = [G[u][v]['color'] for u,v in edges]   # get result as LIST
colors = nx.get_edge_attributes(G,'color').values()   # get result as DICTIONARY
type(colors)
weights = [G[u][v]['weight'] for u,v in edges]

nx.draw(G, pos, edges=edges, edge_color=list(colors), width=weights)

A=nx.to_pandas_adjacency(G)
display(A)
# A=nx.linalg.graphmatrix.adjacency_matrix(G)
