from itertools import combinations

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
        an1 = (at1[0] - vec[0], at1[1] - vec[1])
        an2 = (at2[0] + vec[0], at2[1] + vec[1])
        if all((0 <= x < length) for x in an1):
            antinodes.add(an1)
        if all((0 <= x < length) for x in an2):
            antinodes.add(an2)

print(len(antinodes))
