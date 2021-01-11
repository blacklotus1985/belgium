import networkx as nx
import numpy as np
import string

def draw_matrix(matrix):
    dt = [('len', float)]
    A = np.array([(0, 0.3, 0.4, 0.7),
                  (0.3, 0, 0.9, 0.2),
                  (0.4, 0.9, 0, 0.1),
                  (0.7, 0.2, 0.1, 0)
                  ]) * 10
    A = A.view(dt)

    G = nx.from_numpy_matrix(A)
    G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())), string.ascii_uppercase)))

    G = nx.drawing.nx_agraph.to_agraph(G)

    G.node_attr.update(color="red", style="filled")
    G.edge_attr.update(color="blue", width="2.0")

    G.draw('/tmp/out.png', format='png', prog='neato')

import networkx as nx

# Create a graph
G = nx.Graph()

# distances
D = [ [0, 1], [1, 0],[3,9] ]

labels = {}
for n in range(len(D)):
    for m in range(len(D)-(n+1)):
        G.add_edge(n,n+m+1)

pos=nx.spring_layout(G)

nx.draw(G, pos)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_size=30)

import pylab as plt
plt.show()
