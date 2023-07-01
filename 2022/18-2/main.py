import networkx as ntx

with open("data.txt", "r") as f:
    points = [tuple(int(x) - 1 for x in pt.split(",")) for pt in f.read().splitlines()]

nx = max(points, key=lambda pt: pt[0])[0] + 3
ny = max(points, key=lambda pt: pt[1])[1] + 3
nz = max(points, key=lambda pt: pt[2])[2] + 3

grid = [[[0 for _ in range(nz)] for _ in range(ny)] for _ in range(nx)]

for pt in points:
    grid[pt[0] + 1][pt[1] + 1][pt[2] + 1] = 1

sa = 0
"""
for x, xv in enumerate(grid):
    for y, yv in enumerate(xv):
        for z, zv in enumerate(yv):
            if (zv == 0) and (x != 0) and (grid[x - 1][y][z] == 1) and (x != nx - 1) and (grid[x + 1][y][z] == 1) and (y != 0) and (grid[x][y - 1][z] == 1) and (
                    y != ny - 1) and (grid[x][y + 1][z] == 1) and (z != 0) and (grid[x][y][z - 1] == 1) and (z != nz - 1) and (grid[x][y][z + 1] == 1):
                sa -= 6
"""
G = ntx.Graph()
for x, xv in enumerate(grid):
    for y, yv in enumerate(xv):
        for z, zv in enumerate(yv):
            if zv == 0:
                G.add_node(f"{str(x)},{str(y)},{str(z)}")

for x, xv in enumerate(grid):
    for y, yv in enumerate(xv):
        for z, zv in enumerate(yv):
            if zv == 0:
                bearing = str(x) + str(y) + str(z)
                bearing = f"{str(x)},{str(y)},{str(z)}"
                if (x != 0) and (grid[x - 1][y][z] == 0):
                    G.add_edge(f"{str(x - 1)},{str(y)},{str(z)}", bearing)
                if (x != nx - 1) and (grid[x + 1][y][z] == 0):
                    G.add_edge(f"{str(x + 1)},{str(y)},{str(z)}", bearing)
                if (y != 0) and (grid[x][y - 1][z] == 0):
                    G.add_edge(f"{str(x)},{str(y - 1)},{str(z)}", bearing)
                if (y != ny - 1) and (grid[x][y + 1][z] == 0):
                    G.add_edge(f"{str(x)},{str(y + 1)},{str(z)}", bearing)
                if (z != 0) and (grid[x][y][z - 1] == 0):
                    G.add_edge(f"{str(x)},{str(y)},{str(z - 1)}", bearing)
                if (z != nz - 1) and (grid[x][y][z + 1] == 0):
                    G.add_edge(f"{str(x)},{str(y)},{str(z + 1)}", bearing)

nodes = set(G.nodes()) - ntx.node_connected_component(G, "0,0,0")
for node in nodes:
    nd = node.split(",")
    x, y, z = int(nd[0]), int(nd[1]), int(nd[2])
    grid[x][y][z] = -1

for pt in points:
    x, y, z = pt
    x, y, z = x + 1, y + 1, z + 1
    if (x == 0) or (grid[x - 1][y][z] == 0):
        sa += 1
    if (x == nx - 1) or (grid[x + 1][y][z] == 0):
        sa += 1
    if (y == 0) or (grid[x][y - 1][z] == 0):
        sa += 1
    if (y == ny - 1) or (grid[x][y + 1][z] == 0):
        sa += 1
    if (z == 0) or (grid[x][y][z - 1] == 0):
        sa += 1
    if (z == nz - 1) or (grid[x][y][z + 1] == 0):
        sa += 1

print(sa)
