def part1():
    with open("input.txt", "r", encoding="utf8") as f:
        lines = [list(x) for x in f.read().splitlines()]

    direction = "up"
    done = False
    last_v_index = len(lines) - 1
    last_h_index = len(lines[0]) - 1
    indices = set()
    while not done:
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char == "^":
                    if (direction == "up" and i == 0) or (direction == "down" and i == last_v_index) or (direction == "left" and j == 0) or (direction == "right" and j == last_h_index):
                        lines[i][j] = "X"
                        done = True
                    else:
                        match direction:
                            case "up":
                                if lines[i-1][j] == "#":
                                    direction = "right"
                                else:
                                    lines[i][j] = "X"
                                    lines[i-1][j] = "^"
                                    indices.add((i-1, j))
                            case "right":
                                if lines[i][j+1] == "#":
                                    direction = "down"
                                else:
                                    lines[i][j] = "X"
                                    lines[i][j+1] = "^"
                                    indices.add((i, j+1))
                            case "down":
                                if lines[i+1][j] == "#":
                                    direction = "left"
                                else:
                                    lines[i][j] = "X"
                                    lines[i+1][j] = "^"
                                    indices.add((i+1, j))
                            case "left":
                                if lines[i][j-1] == "#":
                                    direction = "up"
                                else:
                                    lines[i][j] = "X"
                                    lines[i][j-1] = "^"
                                    indices.add((i, j-1))
                    break
            else:
                continue
            break

    print(len(indices))
    return indices

if __name__ == "__main__":
    part1()

