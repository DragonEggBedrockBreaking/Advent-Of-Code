import itertools

with open("input.txt", "r", encoding="utf8") as f:
    coords = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]

print(max((abs(a-c)+1)*(abs(b-d)+1) for (a, b), (c, d) in itertools.combinations(coords, 2)))
