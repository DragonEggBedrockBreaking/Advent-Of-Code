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
    node1, node2 = edge
    merged = f"{node1}+{node2}"
    G.add_node(merged)
    neighbours = set(G.neighbors(node1)) | set(G.neighbors(node2))
    for neighbour in neighbours:
        if neighbour in (node1, node2):
            continue
        G.add_edge(merged, neighbour, weight=min(G.get_edge_data(node1, neighbour)["weight"], G.get_edge_data(node2, neighbour)["weight"]))
    G.remove_node(node1)
    G.remove_node(node2)


G = nx.Graph()
G.add_nodes_from(lines)
G.add_weighted_edges_from([(node1, node2, distance(node1, node2)) for (node1, node2) in itertools.combinations(lines, 2)])

while len(G.nodes) > 2:
    print(len(G.nodes))
    merge(min(nx.get_edge_attributes(G, "weight").items(), key=lambda entry: entry[1])[0])
first, second = tuple(G.edges)[0]
final1, final2 = min(itertools.product(first.split("+"), second.split("+")), key=lambda nodes: distance(nodes[0], nodes[1]))
print(int(final1.split(",")[0]) * int(final2.split(",")[0]))
