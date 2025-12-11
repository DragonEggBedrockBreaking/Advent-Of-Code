import networkx as nx

with open("input.txt", "r", encoding="utf8") as f:
    lines = {line.split(": ")[0]: line.split(": ")[1].split() for line in f.read().splitlines()}

G = nx.DiGraph()
G.add_nodes_from(lines.keys())
G.add_edges_from([(start, end) for start, ends in lines.items() for end in ends])
print(len(tuple(nx.all_simple_paths(G, source="you", target="out"))))