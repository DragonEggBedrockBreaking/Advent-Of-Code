#from itertools import permutations
import networkx as nx
from copy import deepcopy

flow_rate = {}
graph = {}
valves = []
abridged_valves = []
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

# Create a set to store the values
lens = set()


def code(total, i, current, options, processed, processing):
    # Keep iterating until the 30 minutes are over
    while i < 30:
        # Iterate the minutes
        i += 1
        # Go through all the open valves and add their flow rate to the total
        for valve in processed:
            total += flow_rate[valve]
        # If we need to wait longer to go to the next valve, do not complete more
        # actions until this is done
        if processing > 0:
            processing -= 1
            continue
        # If the current valve is not open, open it
        if current not in processed:
            processed.append(current)
        # If the valve is open
        else:
            # If there are no more valves, continue onwards
            if len(options) == 0:
                continue
            # Go through each of the remaining valves
            for option in options:
                # Create a copy of the options list, and remove the option from it
                temp = deepcopy(options)
                temp.remove(option)
                # Work out the distance between this valve and the next one
                distance = distances[(current, option)]
                # Call the functionr recursively, with:
                # - the current total
                # - the current minute count
                # - the next valve
                # - the remaining valves
                # - the open valves
                # - how many more minutes it would take to process the valve
                code(total, i, option, temp, processed, distance - 1)
            # Empty the options list
            options = []
    # Add the total to the set
    lens.add(total)


# Call the function using a total of 0, 0 minutes, AA as the starting
# valve, the valves with flow rate > 0 as the options, and 0 as processing
# (can be anything <= 0)
code(0, 0, "AA", abridged_valves, ["AA"], 0)
print(lens)
# Print the largest value in the list
print(max(lens))
