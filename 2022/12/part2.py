import networkx as nx
from networkx.exception import NetworkXNoPath

start, end = [], 0

with open("data.txt", "r") as f:
    lines = [[char for char in line] for line in f.read().splitlines()]

LEN_LINES = len(lines)
LEN_LINE = len(lines[0])

if any("S" in (match := line) for line in lines):
    lines[lines.index(match)][match.index("S")] = "a"
if any("E" in (match := line) for line in lines):
    ln = lines.index(match)
    ch = match.index("E")
    end = ln * LEN_LINE + ch
    lines[ln][ch] = "z"
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "a":
            start.append(i * LEN_LINE + j)

G = nx.DiGraph()
G.add_nodes_from(range(LEN_LINES * LEN_LINE))

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if (i != 0) and (ord(lines[i - 1][j]) <= ord(char) + 1):
            G.add_edge(i * LEN_LINE + j, (i - 1) * LEN_LINE + j)
        if (i != LEN_LINES - 1) and (ord(lines[i + 1][j]) <= ord(char) + 1):
            G.add_edge(i * LEN_LINE + j, (i + 1) * LEN_LINE + j)
        if (j != 0) and (ord(line[j - 1]) <= ord(char) + 1):
            G.add_edge(i * LEN_LINE + j, i * LEN_LINE + (j - 1))
        if (j != LEN_LINE - 1) and (ord(line[j + 1]) <= ord(char) + 1):
            G.add_edge(i * LEN_LINE + j, i * LEN_LINE + (j + 1))

paths = []
for pos in start:
    try:
        paths.append(nx.shortest_path_length(G, pos, end))
    except NetworkXNoPath:
        continue
print(min(paths))
