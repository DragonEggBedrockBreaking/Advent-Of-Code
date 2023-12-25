import functools

import networkx as nx

with open("input.txt", "r", encoding="utf8") as f:
    lines = {x.split(": ")[0]: x.split(": ")[1].split(" ") for x in f.read().splitlines()}

G = nx.Graph()
for source, targets in lines.items():
    G.add_node(source)
    G.add_nodes_from(targets)
    for target in targets:
        G.add_edge(source, target)

for edge in nx.minimum_edge_cut(G):
    G.remove_edge(*edge)
print(functools.reduce(lambda x, y: x * y, [len(x) for x in nx.connected_components(G)]))
