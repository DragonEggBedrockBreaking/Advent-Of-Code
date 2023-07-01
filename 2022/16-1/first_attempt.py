from itertools import permutations
import networkx as nx

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

# Creates a set for the lengths
lens = set()

def run(permutation):
    # Converts the permutation from a tuple to a list
    permutation = list(permutation)
    # Creates variables for the total and the minutes
    total = 0
    i = 0
    # Stores the current item, and all the valves that are processed every minute
    current = "AA"
    processed = ["AA"]
    # The distance between this valve and the next - i.e. for how many minutes
    # are we moving between two valves that are not adjacent
    processing = 0

    # Keep running until it hits 30 mins
    while i < 30:
        i += 1
        # Go through each open valve and add its flow rate to the total
        for valve in processed:
            total += flow_rate[valve]
        # If we are moving between valves, decrement the minute counter and skip
        # the rest of the code this iteration
        if processing > 0:
            processing -= 1
            continue
        # If the current valve is not open, open the valve and move to the next minute
        if current not in processed:
            processed.append(current)
        # If the current valve is open, we move to the next one
        else:
            # If there are no more left, just keep iterating throught the minutes and
            # increasing the counter
            if len(permutation) == 0:
                continue
            # If there is another one in the permutation, get the next valve
            # Note that we iterate backwards over the permutation, which way we
            # iterate is not important as we will go through every permutation either
            # way
            next = permutation.pop()
            # Calculate the distance between the current valve and the next one
            distance = distances[(current, next)]
            # Set the current one to the next one for next iteration
            current = next
            # If the next valve is not adjacent, it will need to be processed for
            # longer - update the variable
            processing = distance - 1
    # Add the total to the set after the 30 minutes are over
    lens.add(total)


# Run the function for each iteration
for j, permutation in enumerate(permutations(abridged_valves)):
    print(j)
    run(permutation)

# Print the largest value in the iteration
print(max(lens))
