with open("data2.txt", "r") as f:
    line = f.read().splitlines()[0]

grid = [["-" for _ in range(7)]]

item = 0
count = 0
m = 1000000000
#m = 2022
points = []
ln_ind = 0
found = False
x = 0

while count < m:
    print(count)
    shapes = [
        [[[0, 2], [0, 3], [0, 4], [0, 5]], 1],
        [[[0, 3], [1, 2], [1, 3], [1, 4], [2, 3]], 3],
        [[[0, 4], [1, 4], [2, 2], [2, 3], [2, 4]], 3],
        [[[0, 2], [1, 2], [2, 2], [3, 2]], 4],
        [[[0, 2], [0, 3], [1, 2], [1, 3]], 2],
    ]

    item %= 5

    shape = shapes[item]

    for i in range(3 + shape[1]):
        grid.insert(0, ["." for _ in range(7)])

    while True:
        dy = -1 if line[ln_ind] == "<" else 1
        edge = 0 if line[ln_ind] == "<" else 6

        ln_ind = (ln_ind + 1) % len(line)

        for point in shape[0]:
            if (point[1] == edge) or (grid[point[0]][point[1] + dy] != "."):
                break
        else:
            for i in range(len(shape[0])):
                shape[0][i][1] += dy

        can_drop = True
        for point in shape[0]:
            if grid[point[0] + 1][point[1]] != ".":
                can_drop = False
                break
        if can_drop:
            for i in range(len(shape[0])):
                shape[0][i][0] += 1
        else:
            for point in shape[0]:
                grid[point[0]][point[1]] = "#"
            break
    while "#" not in grid[0]:
        del grid[0]

    if not found:
        tup = (item, ln_ind)
        matches = [t for t in points if t == tup]
        if len(matches) > 0:
            found = True
            x = len(grid) - 1
        else:
            points.append((item, ln_ind))
    item += 1
    count += 1

print(x)
print(len(grid) - 1)
