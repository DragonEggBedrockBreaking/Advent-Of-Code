with open("input.txt", "r", encoding="utf8") as f:
    lines = [list(line) for line in f.read().splitlines()]
energised = set()
visited = set()
starting_direction = "R"
if lines[0][0] in "\\|":
    starting_direction = "D"
beams = [(0, 0, starting_direction)]


def traverse(x, y, direction):
    while True:
        energised.add((x, y))
        if (x, y, direction) in visited:
            return
        visited.add((x, y, direction))
        match direction:
            case "R":
                if y + 1 >= len(lines[x]):
                    return
                y += 1
                match lines[x][y]:
                    case "\\":
                        direction = "D"
                    case "/":
                        direction = "U"
                    case "|":
                        direction = "U"
                        beams.append((x, y, "D"))
            case "L":
                if y - 1 < 0:
                    return
                y -= 1
                match lines[x][y]:
                    case "\\":
                        direction = "U"
                    case "/":
                        direction = "D"
                    case "|":
                        direction = "U"
                        beams.append((x, y, "D"))
            case "U":
                if x - 1 < 0:
                    return
                x -= 1
                match lines[x][y]:
                    case "\\":
                        direction = "L"
                    case "/":
                        direction = "R"
                    case "-":
                        direction = "L"
                        beams.append((x, y, "R"))
            case "D":
                if x + 1 >= len(lines):
                    return
                x += 1
                match lines[x][y]:
                    case "\\":
                        direction = "R"
                    case "/":
                        direction = "L"
                    case "-":
                        direction = "L"
                        beams.append((x, y, "R"))


while beams:
    traverse(beams[0][0], beams[0][1], beams.pop(0)[2])
print(len(energised))
