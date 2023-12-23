import networkx as nx
import copy

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()
START, END = (0, 1), (len(lines) - 1, len(lines[0]) - 2)
G = nx.Graph()
G.add_nodes_from((i, j) for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j] != "#")
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if (i, j) in (START, END):
            continue
        match char:
            case "." | ">" | "<" | "^" | "v":
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    if lines[i + di][j + dj] != "#":
                        G.add_edge((i, j), (i + di, j + dj), weight=1)

for node in copy.deepcopy(G.nodes):
    neighbours = list(G.neighbors(node))
    if len(neighbours) == 2:
        left_weight = G.get_edge_data(node, neighbours[0])["weight"]
        right_weight = G.get_edge_data(node, neighbours[1])["weight"]
        G.add_edge(neighbours[0], neighbours[1], weight=left_weight + right_weight)
        G.remove_node(node)

max_len = 0
for path in nx.all_simple_paths(G, START, END):
    length = sum(G.get_edge_data(path[i], path[i + 1])["weight"] for i in range(len(path) - 1))
    max_len = max(max_len, length)
print(max_len)
