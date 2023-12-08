from math import gcd

with open("input.txt") as f:
    lines = [line.replace(")", "") for line in f.read().splitlines()]

data = {x.split(" =")[0]: tuple(x.split("(")[1].split(", ")) for x in lines[2:]}
nodes = [node for node in data.keys() if node[2] == "A"]
for j, node in enumerate(nodes):
    progression = lines[0]
    i = 0
    while not nodes[j].endswith("Z"):
        nodes[j] = data[nodes[j]][0 if progression[0] == "L" else 1]
        progression = progression[1:] + progression[0]
        i += 1
    nodes[j] = i

lcm = 1
for n in nodes:
    lcm = lcm * n // gcd(lcm, n)
print(lcm)
