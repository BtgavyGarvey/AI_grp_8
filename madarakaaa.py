from turtle import position
import networkx as nx
import matplotlib.pyplot as plt
import _random

# create a directed graph representing Madaraka Estate
G = nx.DiGraph()

# add nodes
G.add_node('Sports Complex')
G.add_node('Siwaka')
G.add_node('Phase 1A')
G.add_node('Phase 1B')
G.add_node('STC')
G.add_node('Phase 2')
G.add_node('J1')
G.add_node('Mada')
G.add_node('Parking Lot')

G.add_nodes_from([])

print(nx.info(G))

# add edges

G.add_edge('Sports Complex', 'Siwaka', weight=450)
G.add_edge('Siwaka', 'Phase 1A', weight=10)
G.add_edge('Siwaka', 'Phase 1B', weight=850)
G.add_edge('Phase 1A', 'Mada', weight=100)
G.add_edge('Phase 1A', 'Phase 1B', weight=112)
G.add_edge('Phase 1B', 'Phase 2', weight=50)
G.add_edge('Phase 1B', 'STC', weight=600)
G.add_edge('Phase 2', 'J1', weight=500)
G.add_edge('Phase 2', 'Phase 3', weight=50)
G.add_edge('STC', 'Phase 3', weight=250)
G.add_edge('STC', 'Parking Lot', weight=850)
G.add_edge('Mada', 'Phase 1A', weight=700)
G.add_edge('Mada', 'Parking Lot', weight=350)
G.add_edge('Phase 3', 'Parking Lot', weight=1)

G.add_edges_from([('Sports Complex', 'Siwaka'), ('Siwaka', 'Phase 1A'), ('Siwaka', 'Phase 1B'), ('Phase 1A', 'Mada'),
                  ('Phase 1A', 'Phase 1B'),
                  ('Phase 1B', 'Phase 2'), ('Phase 1B', 'STC'), ('Phase 2', 'J1'), ('Phase 2', 'J1'),
                  ('STC', 'Phase 2'), ('STC', 'Parking Lot'), ('Mada', 'Phase 1A')
                     , ('Mada', 'Parking Lot'), ('Phase 3', 'Parking Lot')])

# Views
print("G.nodes =", G.nodes)
print("G.edges =", G.edges)
print("G.degree =", G.degree)
print("G.adj =", G.adj)

pos = nx.random_layout(G)

nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='black')
nx.draw_networkx_nodes(G, pos, )
nx.draw_networkx_labels(G, pos)

# Draw Graph
nx.draw(G, with_labels=1)
plt.show()
