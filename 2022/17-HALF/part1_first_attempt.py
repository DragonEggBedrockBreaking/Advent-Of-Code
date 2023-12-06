with open("data2.txt", "r") as f:
    line = f.read().splitlines()[0]

grid = []
shapes = [
    [[".", ".", "#", "#", "#", "#", "."]],

    [[".", ".", ".", "#", ".", ".", "."],
     [".", ".", "#", "#", "#", ".", "."],
     [".", ".", ".", "#", ".", ".", "."]],

    [[".", ".", ".", ".", "#", ".", "."],
     [".", ".", ".", ".", "#", ".", "."],
     [".", ".", "#", "#", "#", ".", "."]],

    [[".", ".", "#", ".", ".", ".", "."],
     [".", ".", "#", ".", ".", ".", "."],
     [".", ".", "#", ".", ".", ".", "."],
     [".", ".", "#", ".", ".", ".", "."]],

    [[".", ".", "#", "#", ".", ".", "."],
     [".", ".", "#", "#", ".", ".", "."]]
]

item = 0
count = 0
dir_ind = -1

while count < 5:
    if item == 5:
        item = 0

    shape = shapes[item]
    for i in range(3):
        grid.insert(0, ["." for _ in range(7)])
    for row in reversed(shape):
        grid.insert(0, row)

    while True:
        dir_ind += 1
        if dir_ind == len(line):
            dir_ind = 0
        direction = line[dir_ind]
        match direction:
            case "<":
                can_go = True
                for i in range(len(shape)):
                    if grid[i][0] != ".":
                        can_go = False
                        break
                if can_go:
                    for i in range(len(shape)):
                        for j in range(1, 7):
                            grid[i][j - 1] = grid[i][j]
                            grid[i][j] = "."
            case ">":
                can_go = True
                for i in range(len(shape)):
                    if grid[i][-1] != ".":
                        can_go = False
                        break
                if can_go:
                    for i in range(len(shape)):
                        for j in range(5, -1, -1):
                            grid[i][j + 1] = grid[i][j]
                            grid[i][j] = "."
        if ["." for _ in range(7)] in grid:
            for i in range(len(shape) - 1, -1, -1):
                grid[i + 1] = grid[i]
            print("#" in grid[0])
            print(grid[0])
            del grid[0]
        else:
            break
    item += 1
    count += 1

for line in grid:
    print(line)
