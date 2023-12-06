from copy import deepcopy
import networkx as nx

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

lens = []


def code(total, i, current, options, processed, processing):
    if i >= 26:
        lens.append((total, tuple(processed)))
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
lens.sort()
print(len(lens))
total = 0
new = []
totals = [0]
i = 0
for tot1, proc1 in reversed(lens):
    i += 1
    print(i)
    for tot2, proc2 in reversed(lens):
        if tot2 > tot1:
            continue
        if len(set(proc1[1:]).intersection(set(proc2[1:]))) == 0:
            tot = tot1 + tot2
            print(tot)
            if tot <= max(totals):
                break
            totals.append(tot)
print(max(totals))
