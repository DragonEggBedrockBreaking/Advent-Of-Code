import networkx as nx

with open("input.txt") as f:
    lines = [list(x) for x in f.read().splitlines()]

G = nx.Graph()
nodes = [i*len(line)+j for i, line in enumerate(lines) for j in range(len(line))]
G.add_nodes_from(nodes)

start = ""
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        node_num = i*len(line)+j
        match char:
            case ".":
                continue
            case "S":
                start = node_num
            case "-":
                if j > 0 and line[j-1] in "-LFS":
                    G.add_edge(node_num, node_num - 1)
                if j < len(line) - 1 and line[j+1] in "-J7S":
                    G.add_edge(node_num, node_num + 1)
            case "|":
                if i > 0 and lines[i-1][j] in "|F7S":
                    G.add_edge(node_num, node_num - len(line))
                if i < len(lines) - 1 and lines[i+1][j] in "|JLS":
                    G.add_edge(node_num, node_num + len(line))
            case "L":
                if i > 0 and lines[i-1][j] in "|F7S":
                    G.add_edge(node_num, node_num - len(line))
                if j < len(line) - 1 and line[j+1] in "-J7S":
                    G.add_edge(node_num, node_num + 1)
            case "J":
                if i > 0 and lines[i-1][j] in "|F7S":
                    G.add_edge(node_num, node_num - len(line))
                if j > 0 and line[j-1] in "-LFS":
                    G.add_edge(node_num, node_num - 1)
            case "7":
                if i < len(lines) - 1 and lines[i+1][j] in "|JLS":
                    G.add_edge(node_num, node_num + len(line))
                if j > 0 and line[j-1] in "-LFS":
                    G.add_edge(node_num, node_num - 1)
            case "F":
                if i < len(lines) - 1 and lines[i+1][j] in "|JLS":
                    G.add_edge(node_num, node_num + len(line))
                if j < len(line) - 1 and line[j+1] in "-J7S":
                    G.add_edge(node_num, node_num + 1)

paths = nx.single_source_shortest_path_length(G, start)
biggest = max(paths.values())
print(biggest)
