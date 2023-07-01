import networkx as nx
from copy import deepcopy
from functools import lru_cache

flow_rate = {"": 0}
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


@lru_cache(maxsize=2**20)
def code(total, i, current_p, current_e, options, processed, processing_p, processing_e):
    if i >= 26:
        lens.add(total)
        return
    i += 1
    for valve in processed:
        total += flow_rate[valve]
    p_opt, e_opt = 0, 0
    if processing_p > 0:
        p_opt = 1
        processing_p -= 1
    elif current_p not in processed:
        p_opt = 1
        processed = list(processed)
        processed.append(current_p)
        processed = tuple(processed)
    else:
        p_opt = 2 if len(options) == 0 else 3
    if processing_e > 0:
        e_opt = 1
        processing_e -= 1
    elif current_e not in processed:
        e_opt = 1
        processed = list(processed)
        processed.append(current_e)
        processed = tuple(processed)
    else:
        e_opt = 2 if len(options) == 0 else 3
    if (p_opt < 3) and (e_opt < 3):
        code(
            total,
            i,
            current_p,
            current_e,
            options,
            deepcopy(processed),
            processing_p,
            processing_e)
    elif e_opt < 3:
        for option in options:
            temp = list(deepcopy(options))
            temp.remove(option)
            distance = distances[(current_p, option)]
            code(total, i, option, current_e, tuple(temp), deepcopy(processed), distance - 1, processing_e)
    elif p_opt < 3:
        for option in options:
            temp = list(deepcopy(options))
            temp.remove(option)
            distance = distances[(current_e, option)]
            code(total, i, current_p, option, tuple(temp), deepcopy(processed), processing_p, distance - 1)
    else:
        if len(options) > 1:
            for option_p in options:
                for option_e in options:
                    if option_p == option_e:
                        continue
                    temp = list(deepcopy(options))
                    temp.remove(option_p)
                    temp.remove(option_e)
                    distance_p = distances[(current_p, option_p)]
                    distance_e = distances[(current_e, option_e)]
                    code(
                        total,
                        i,
                        option_p,
                        option_e,
                        tuple(temp),
                        deepcopy(processed),
                        distance_p - 1,
                        distance_e - 1)
        else:
            distance_p = distances[(current_p, options[0])]
            distance_e = distances[(current_e, options[0])]
            if distance_p >= distance_e:
                code(
                    total,
                    i,
                    options[0],
                    current_e,
                    (),
                    deepcopy(processed),
                    distance_p - 1,
                    processing_e)
            else:
                code(
                    total,
                    i,
                    current_p,
                    options[0],
                    (),
                    deepcopy(processed),
                    processing_p,
                    distance_e - 1)


code(0, 0, "AA", "AA", tuple(abridged_valves), ("", "AA"), 0, 0)
print(max(lens))
