import networkx as nx

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()
START, END = (0, 1), (len(lines) - 1, len(lines[0]) - 2)
G = nx.DiGraph()
G.add_nodes_from((i, j) for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j] != "#")
G.add_edge(START, (1, 1))
G.add_edge(END, (len(lines) - 2, len(lines[0]) - 2))
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if (i, j) in (START, END):
            continue
        match char:
            case ".":
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    if lines[i + di][j + dj] == ".":
                        G.add_edge((i, j), (i + di, j + dj))
            case "^":
                G.add_edge((i + j, j), (i, j))
                G.add_edge((i, j), (i - 1, j))
            case "v":
                G.add_edge((i - 1, j), (i, j))
                G.add_edge((i, j), (i + 1, j))
            case ">":
                G.add_edge((i, j - 1), (i, j))
                G.add_edge((i, j), (i, j + 1))
            case "<":
                G.add_edge((i, j + 1), (i, j))
                G.add_edge((i, j), (i, j - 1))

paths = nx.all_simple_paths(G, START, END)
lengths = [len(path) for path in paths]
print(len(lengths))
print(max(lengths) - 1)
