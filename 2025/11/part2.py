import networkx as nx

with open("input.txt", "r", encoding="utf8") as f:
    lines = {line.split(": ")[0]: line.split(": ")[1].split() for line in f.read().splitlines()}

G = nx.DiGraph()
nodes = lines.keys()
G.add_nodes_from(nodes)
G.add_edges_from([(start, end) for start, ends in lines.items() for end in ends])


def count_paths(start, end):
    routes = {node: int(node == start) for node in nodes}
    routes["out"] = 0
    for u in nx.topological_sort(G):
        for v in G.successors(u):
            routes[v] += routes[u]
    return routes[end]


print(count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out") +
      count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out"))
