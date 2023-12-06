with open("data.txt", "r") as f:
    points = [tuple(int(x) for x in pt.split(",")) for pt in f.read().splitlines()]

nx = max(points, key=lambda pt: pt[0])[0] + 2
ny = max(points, key=lambda pt: pt[1])[1] + 2
nz = max(points, key=lambda pt: pt[2])[2] + 2

grid = [[[0 for _ in range(nz)] for _ in range(ny)] for _ in range(nx)]

for pt in points:
    grid[pt[0]][pt[1]][pt[2]] = 1

sa = 0
for pt in points:
    x, y, z = pt
    if (x == 0) or (grid[x - 1][y][z] == 0):
        sa += 1
    if (x == nx) or (grid[x + 1][y][z] == 0):
        sa += 1
    if (y == 0) or (grid[x][y - 1][z] == 0):
        sa += 1
    if (y == ny) or (grid[x][y + 1][z] == 0):
        sa += 1
    if (z == 0) or (grid[x][y][z - 1] == 0):
        sa += 1
    if (z == nz) or (grid[x][y][z + 1] == 0):
        sa += 1

print(sa)
