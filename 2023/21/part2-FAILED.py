import numpy as np

with open("input.txt", "r") as f:
    lines = [list(l) * 11 for l in f.read().splitlines()] * 11
S = (720, 720)


def traverse(x, y, depth=1):
    if depth > distance + 1:
        points.add((x, y))
        return
    if (x, y, depth) in visited:
        return
    visited.add((x, y, depth))
    if x > 0 and lines[x-1][y] != "#":
        queue.append((x-1, y, depth+1))
    if x < len(lines)-1 and lines[x+1][y] != "#":
        queue.append((x+1, y, depth+1))
    if y > 0 and lines[x][y-1] == ".":
        queue.append((x, y-1, depth+1))
    if y < len(lines[0])-1 and lines[x][y+1] != "#":
        queue.append((x, y+1, depth+1))


steps = [65, 65 + 131, 65 + 2 * 131]
y = []
for distance in steps:
    visited = set()
    points = set()
    queue = [(S[0], S[1], 1)]
    while queue:
        print(len(queue))
        traverse(*queue.pop(0))
    y.append(len(points))

print(*y)
vandermonde = np.vander((0, 1, 2), 3)
coefficients = np.linalg.solve(vandermonde, y)
print(int(coefficients[0]*202300**2 + coefficients[1]*202300 + coefficients[2]))
