import itertools
import math
import networkx as nx

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()


def distance(node1, node2):
    a, b, c = map(int, node1.split(","))
    x, y, z = map(int, node2.split(","))
    return math.sqrt((a-x)**2 + (b-y)**2 + (c-z)**2)


def merge(edge):
    node1, node2, _ = edge
    loc1, loc2 = locations[node1], locations[node2]
    if loc1 == loc2:
        return
    merged = f"{loc1}+{loc2}"
    for node in merged.split("+"):
        locations[node] = merged
    G.add_node(merged)
    neighbours = set(G.neighbors(loc1)) | set(G.neighbors(loc2))
    for neighbour in neighbours:
        if neighbour in (loc1, loc2):
            continue
        G.add_edge(merged, neighbour)
    G.remove_node(loc1)
    G.remove_node(loc2)


G = nx.Graph()
G.add_nodes_from(lines)
edges = [(node1, node2, distance(node1, node2)) for (node1, node2) in itertools.combinations(lines, 2)]
edges.sort(key=lambda edge: edge[2])
G.add_edges_from(map(lambda edge: edge[:2], edges))
locations = {node: node for node in lines}
for e in edges[:1000]:
    merge(e)
print(math.prod(sorted([node.count("+")+1 for node in G.nodes], reverse=True)[:3]))
