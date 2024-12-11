import copy
from part1 import part1

indices = part1()

with open("input.txt", "r") as f:
    lines = [list(x) for x in f.read().splitlines()]

last_v_index = len(lines) - 1
last_h_index = len(lines[0]) - 1


def simulate(ls):
    direction = "up"
    while True:
        for i, line in enumerate(ls):
            for j, char in enumerate(line):
                if char.endswith("^"):
                    if (direction == "up" and i == 0) or (direction == "down" and i == last_v_index) or (direction == "left" and j == 0) or (direction == "right" and j == last_h_index):
                        return False
                    else:
                        match direction:
                            case "up":
                                if ls[i-1][j] == "#":
                                    direction = "right"
                                else:
                                    ls[i][j] = ls[i][j] + "U"
                                    if "U" in ls[i-1][j] or ("R" in ls[i-1][j] and ls[i-2][j] == "#"):
                                        return True
                                    ls[i-1][j] = ls[i-1][j] + "^"
                            case "right":
                                if ls[i][j+1] == "#":
                                    direction = "down"
                                else:
                                    ls[i][j] = ls[i][j] + "R"
                                    if "R" in ls[i][j+1] or ("D" in ls[i][j+1] and ls[i][j+2] == "#"):
                                        return True
                                    ls[i][j+1] = ls[i][j+1] + "^"
                            case "down":
                                if ls[i+1][j] == "#":
                                    direction = "left"
                                else:
                                    ls[i][j] = ls[i][j] + "D"
                                    if "D" in ls[i+1][j] or ("L" in ls[i+1][j] and ls[i+2][j] == "#"):
                                        return True
                                    ls[i+1][j] = ls[i+1][j] + "^"
                            case "left":
                                if ls[i][j-1] == "#":
                                    direction = "up"
                                else:
                                    ls[i][j] = ls[i][j] + "L"
                                    if "L" in ls[i][j-1] or ("U" in ls[i][j-1] and ls[i][j-2] == "#"):
                                        return True
                                    ls[i][j-1] = ls[i][j-1] + "^"
                    break
            else:
                continue
            break


count = 0
for index, (x, y) in enumerate(indices):
    print(index)
    if lines[x][y] != "^":
        new_list = copy.deepcopy(lines)
        new_list[x][y] = "#"
        if simulate(new_list):
            count += 1

print(count)