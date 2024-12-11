with open("input.txt", "r", encoding="utf8") as f:
    lines = [[int(y) if y != "." else y for y in x] for x in f.read().splitlines()]

trailheads = set()
for i, line in enumerate(lines):
    for j, point in enumerate(line):
        if point == 0:
            trailheads.add((i, j))


def search(x, y, val):
    if val == 9:
        ends.add((x, y))
        return
    if x > 0 and lines[x-1][y] == val+1:
        search(x-1, y, val+1)
    if x < len(lines)-1 and lines[x+1][y] == val+1:
        search(x+1, y, val+1)
    if y > 0 and lines[x][y-1] == val+1:
        search(x, y-1, val+1)
    if y < len(lines[0])-1 and lines[x][y+1] == val+1:
        search(x, y+1, val+1)


total = 0
for a, b in trailheads:
    ends = set()
    search(a, b, 0)
    total += len(ends)

print(total)
