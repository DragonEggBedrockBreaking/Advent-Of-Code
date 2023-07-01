import networkx as nx
from copy import deepcopy

flow_rate = {}
graph = {}
valves = []
abridged_valves = []
distances = {}

with open("data.txt", "r") as f:
    for line in f.read().splitlines():
        val = line.split()[1]
        flow_rate[val] = int(line.split(";")[0].split("=")[1])
        if "," in line:
            graph[val] = line.split("valves ")[1].split(", ")
        else:
            graph[val] = [line.split()[-1]]
        valves.append(val)

for i, v in enumerate(valves):
    if flow_rate[v] > 0:
        abridged_valves.append(v)

g = nx.Graph()
for valve in valves:
    g.add_node(valve)

for key in graph.keys():
    for val in graph[key]:
        g.add_edge(key, val)

for first in valves:
    for second in valves:
        if (first != second) and ((flow_rate[first] > 0) or (first == "AA")) and (
                (flow_rate[second] > 0) or (second == "AA")):
            distances[(first, second)] = nx.shortest_path_length(g, first, second)

lens = set()


def code(total, i, current, options, processed, processing):
    if i >= 30:
        lens.add(total)
        if current in processed:
            processed.remove(current)
        return
    i += 1
    for valve in processed:
        total += flow_rate[valve]
    if processing > 0:
        code(total, i, current, options, processed, processing - 1)
    elif current not in processed:
        processed.append(current)
        code(total, i, current, options, processed, processing)
    elif len(options) == 0:
        code(total, i, current, options, processed, processing)
    else:
        for option in options:
            temp = deepcopy(options)
            temp.remove(option)
            distance = distances[(current, option)]
            code(total, i, option, temp, processed, distance - 1)
    if current in processed:
        processed.remove(current)


code(0, 0, "AA", abridged_valves, ["AA"], 0)
print(max(lens))
