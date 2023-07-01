import re
with open("data.txt", "r") as f:
    lines = f.read().splitlines()
input = lines.pop()
input = re.findall(r"\d+|\D+", input)
lines.remove("")
grid = []
for i, line in enumerate(lines):
    grid.append(list(line))
mx = max([len(row) for row in grid])
grid.insert(0, [" " for _ in range(mx + 2)])
grid.append([" " for _ in range(mx + 2)])
for i in range(len(grid)):
    while len(grid[i]) < mx + 1:
        grid[i].append(" ")
    grid[i].insert(0, " ")
direction = 0
pos = [1, grid[1].index(".")]
for char in input:
    if char.isnumeric():
        for i in range(int(char)):
            match direction:
                case 0:
                    match grid[pos[0]][pos[1] + 1]:
                        case ".":
                            pos[1] += 1
                        case " ":
                            dot = grid[pos[0]].index(".")
                            if "#" not in grid[pos[0]]:
                                pos[1] = dot
                                continue
                            hash = grid[pos[0]].index("#")
                            pos[1] = dot if dot < hash else pos[1]
                case 1:
                    match grid[pos[0] + 1][pos[1]]:
                        case ".":
                            pos[0] += 1
                        case " ":
                            dot = next(i for i, row in enumerate(grid) if row[pos[1]] == ".")
                            try:
                                hash = next(i for i, row in enumerate(grid) if row[pos[1]] == "#")
                            except StopIteration:
                                pos[0] = dot
                                continue
                            pos[0] = dot if dot < hash else pos[0]
                case 2:
                    match grid[pos[0]][pos[1] - 1]:
                        case ".":
                            pos[1] -= 1
                        case " ":
                            dot = "".join(grid[pos[0]]).rindex(".")
                            if "#" not in grid[pos[0]]:
                                pos[1] = dot
                                continue
                            hash = "".join(grid[pos[0]]).rindex("#")
                            pos[1] = dot if dot > hash else pos[1]
                case 3:
                    match grid[pos[0] - 1][pos[1]]:
                        case ".":
                            pos[0] -= 1
                        case " ":
                            dot = len(grid) - next(i for i,
                                                   row in enumerate(reversed(grid)) if row[pos[1]] == ".") - 1
                            try:
                                hash = len(grid) - next(i for i,
                                                        row in enumerate(reversed(grid)) if row[pos[1]] == "#") - 1
                            except StopIteration:
                                pos[0] = dot
                                continue
                            pos[0] = dot if dot > hash else pos[0]
    else:
        match char:
            case "R":
                direction = (direction + 1) % 4
            case "L":
                direction = (direction - 1) % 4

print(pos[0] * 1000 + pos[1] * 4 + direction)
