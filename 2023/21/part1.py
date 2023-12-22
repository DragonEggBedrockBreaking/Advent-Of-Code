with open("input.txt", "r") as f:
    lines = [list(l) for l in f.read().splitlines()]
DISTANCE = 64
S = (0, 0)
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "S":
            S = (i, j)
            break


def traverse(x, y, depth=1):
    if depth > DISTANCE:
        points.add((x, y))
        return
    if (x, y, depth) in visited:
        return
    visited.add((x, y, depth))
    if x > 0 and lines[x-1][y] != "#":
        queue.append((x-1, y, depth+1))
    if x < len(lines)-1 and lines[x+1][y] != "#":
        queue.append((x+1, y, depth+1))
    if y > 0 and lines[x][y-1] != "#":
        queue.append((x, y-1, depth+1))
    if y < len(lines[0])-1 and lines[x][y+1] != "#":
        queue.append((x, y+1, depth+1))


visited = set()
points = set()
queue = [(S[0], S[1], 1)]
while queue:
    traverse(*queue.pop(0))
print(len(points))
