with open("input.txt", "r", encoding="utf8") as f:
    lines = [list(line) for line in f.read().splitlines()]


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


energised_nums = []
starting = []
for i in range(len(lines[0])):
    match lines[0][i]:
        case "." | "|":
            starting.append((0, i, "D"))
        case "-":
            starting.append((0, i, "R"))
            starting.append((0, i, "L"))
        case "\\":
            starting.append((0, i, "R"))
        case "/":
            starting.append((0, i, "L"))
    match lines[-1][i]:
        case "." | "|":
            starting.append((len(lines) - 1, i, "U"))
        case "-":
            starting.append((len(lines) - 1, i, "R"))
            starting.append((len(lines) - 1, i, "L"))
        case "\\":
            starting.append((len(lines) - 1, i, "L"))
        case "/":
            starting.append((len(lines) - 1, i, "R"))
for i in range(len(lines)):
    match lines[i][0]:
        case "." | "-":
            starting.append((i, 0, "R"))
        case "|":
            starting.append((i, 0, "D"))
            starting.append((i, 0, "U"))
        case "\\":
            starting.append((i, 0, "D"))
        case "/":
            starting.append((i, 0, "U"))
    match lines[i][-1]:
        case "." | "-":
            starting.append((i, len(lines[i]) - 1, "L"))
        case "|":
            starting.append((i, len(lines[i]) - 1, "D"))
            starting.append((i, len(lines[i]) - 1, "U"))
        case "\\":
            starting.append((i, len(lines[i]) - 1, "U"))
        case "/":
            starting.append((i, len(lines[i]) - 1, "D"))
for start in starting:
    energised, visited, beams = set(), set(), [start]
    while beams:
        traverse(beams[0][0], beams[0][1], beams.pop(0)[2])
    energised_nums.append(len(energised))

print(max(energised_nums))
