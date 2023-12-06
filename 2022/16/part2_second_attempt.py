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
        orders[total] = tuple(processed[1:])
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


code(0, 0, "AA", valves, ["AA"], 0)
order = list(orders[max(lens)])
print(order)

total, i = 0, 0
current_p, current_e = "AA", "AA"
processed = []
processing_p, processing_e = 0, 0
while i < 26:
    print(i)
    i += 1
    for valve in processed:
        total += flow_rate[valve]
    next_p, next_e = False, False
    if processing_p > 0:
        processing_p -= 1
    elif current_p not in processed:
        processed.append(current_p)
    elif len(order) > 0:
        next_p = True
    if processing_e > 0:
        processing_e -= 1
    elif current_e not in processed:
        processed.append(current_e)
    elif len(order) > 0:
        next_e = True
    if next_p and not next_e:
        next = order[0]
        del order[0]
        dist = distances[(current_p, next)]
        current_p = next
        processing_p = dist - 1
    elif next_e and not next_p:
        next = order[0]
        del order[0]
        dist = distances[(current_e, next)]
        current_e = next
        processing_e = dist - 1
    elif next_p and next_e:
        if len(order) > 1:
            next1 = order[0]
            next2 = order[1]
            del order[0]
            del order[1]
            dist_p1 = distances[(current_p, next1)]
            dist_p2 = distances[(current_p, next2)]
            dist_e1 = distances[(current_e, next1)]
            dist_e2 = distances[(current_e, next2)]
            if dist_p1 + dist_e1 <= dist_e1 + dist_e2:
                current_p = next1
                current_e = next2
                processing_p = dist_p1 - 1
                processing_e = dist_e1 - 1
            else:
                current_p = next2
                current_e = next1
                processing_p = dist_p2 - 1
                processing_e = dist_e2 - 1
        else:
            next = order[0]
            order = []
            dist_p = distances[(current_p, next)]
            dist_e = distances[(current_e, next)]
            if dist_p <= dist_e:
                current_p = next
                processing_p = dist_p
            else:
                current_e = next
                processing_e = dist_e

print(total)
