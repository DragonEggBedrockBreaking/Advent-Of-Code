from itertools import combinations
from math import gcd

signals = {}
antinodes = set()
length = 0

with open("input.txt", "r", encoding="utf8") as f:
    for i, line in enumerate(f):
        if i == 0:
            length = len(line.strip())
        for j, char in enumerate(line.strip()):
            if char != ".":
                if char in signals.keys():
                    signals[char].append((i, j))
                else:
                    signals[char] = [(i, j)]

for antennas in signals.values():
    for at1, at2 in combinations(antennas, 2):
        vec = (at2[0] - at1[0], at2[1] - at1[1])
        hcf = gcd(vec[0], vec[1])
        unit = (vec[0] // hcf, vec[1] // hcf)
        pt = (at1[0] - vec[0], at1[1] - vec[1])
        while all((0 <= x < length) for x in pt):
            antinodes.add(pt)
            pt = (pt[0] - vec[0], pt[1] - vec[1])
        pt = (at1[0] + vec[0], at1[1] + vec[1])
        while all((0 <= x < length) for x in pt):
            antinodes.add(pt)
            pt = (pt[0] + vec[0], pt[1] + vec[1])
        antinodes.add(at1)

print(len(antinodes))
