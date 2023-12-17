import networkx as nx

with open("input.txt", "r", encoding="utf8") as f:
    lines = [[int(i) for i in line] for line in f.read().splitlines()]

G = nx.Graph()
for i, line in enumerate(lines):
    for j in range(len(line)):
        G.add_node((i, j))
for i, line in enumerate(lines):
    for j in range(len(line)):
        if i > 0:
            G.add_edge((i, j), (i-1, j), weight=lines[i-1][j])
        if i < len(lines[0]) - 1:
            G.add_edge((i, j), (i+1, j), weight=lines[i+1][j])
        if j > 0:
            G.add_edge((i, j), (i, j-1), weight=lines[i][j-1])
        if j < len(lines) - 1:
            G.add_edge((i, j), (i, j+1), weight=lines[i][j+1])
