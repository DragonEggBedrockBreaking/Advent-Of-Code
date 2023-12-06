import networkx as nx
from copy import deepcopy

flow_rate = {}
graph = {}
valves = []
distances = {}

with open("data2.txt", "r") as f:
    for line in f.read().splitlines():
        val = line.split()[1]
        flow_rate[val] = int(line.split(";")[0].split("=")[1])
        if "," in line:
            graph[val] = line.split("valves ")[1].split(", ")
        else:
            graph[val] = [line.split()[-1]]
        valves.append(val)

g = nx.Graph()
for valve in valves:
    g.add_node(valve)

for key in graph.keys():
    for val in graph[key]:
        g.add_edge(key, val)

for first in valves:
    for second in valves:
        distances[(first, second)] = nx.shortest_path_length(g, first, second)

lens = set()
orders = {}


def code(total, i, current, options, processed, processing):
    if i >= 26:
        lens.add(total)
        orders[total] = tuple(processed)
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


valves.remove("AA")
code(0, 0, "AA", valves, ["AA"], 0)
print("done first")
order = set(orders[max(lens)])
mx = max(lens)
lens = set()
code(0, 0, "AA", list(set(valves) - order), ["AA"], 0)
print(mx)
print(max(lens))
print(max(lens) + mx)
