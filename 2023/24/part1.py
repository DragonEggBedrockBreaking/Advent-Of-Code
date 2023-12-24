from itertools import combinations
from z3 import Real, Solver, sat

with open("input.txt", "r", encoding="utf8") as f:
    lines = []
    for x in f.read().splitlines():
        first, second = x.split(" @ ")
        lines.append((tuple(map(int, first.replace(" ", "").split(",")[:2])), tuple(map(int, second.replace(" ", "").split(",")[:2]))))

total = 0
for (pos1, vel1), (pos2, vel2) in combinations(lines, 2):
    x = Real("x")
    y = Real("y")
    s = Solver()
    s.add(y == pos1[1] + vel1[1] * ((x - pos1[0]) / vel1[0]))
    s.add(y == pos2[1] + vel2[1] * ((x - pos2[0]) / vel2[0]))
    s.add(200000000000000 <= x, x <= 400000000000000, 200000000000000 <= y, y <= 400000000000000)
    s.add((x - pos1[0]) / vel1[0] >= 0, (x - pos2[0]) / vel2[0] >= 0)
    if s.check() == sat:
        total += 1
print(total)
