with open("data.txt", "r") as f:
    lines = [list(line) for line in f.read().splitlines()]
for _ in range(10):
    lines.insert(0, ["." for _ in range(len(lines[0]))])
    lines.append(["." for _ in range(len(lines[0]))])
for i in range(len(lines)):
    for _ in range(10):
        lines[i].insert(0, ".")
        lines[i].append(".")
elves = []
for i, line in enumerate(lines):
    for j, pos in enumerate(line):
        if pos == "#":
            elves.append((i, j))
proposed = elves.copy()
previous = [(0, 0) for _ in elves]
order = ["N", "S", "W", "E"]


def translate(point, direction):
    match direction:
        case "N":
            return (point[0] - 1, point[1])
        case "NW":
            return (point[0] - 1, point[1] - 1)
        case "NE":
            return (point[0] - 1, point[1] + 1)
        case "S":
            return (point[0] + 1, point[1])
        case "SW":
            return (point[0] + 1, point[1] - 1)
        case "SE":
            return (point[0] + 1, point[1] + 1)
        case "W":
            return (point[0], point[1] - 1)
        case "E":
            return (point[0], point[1] + 1)
    return point


def elves_present(point, direction):
    directions = ()
    match direction:
        case "N":
            directions = ("N", "NW", "NE")
        case "S":
            directions = ("S", "SW", "SE")
        case "W":
            directions = ("W", "NW", "SW")
        case "E":
            directions = ("E", "NE", "SE")
    for dir in directions:
        if translate(point, dir) in elves:
            return True
    return False


iterations = 0
while previous != elves:
    previous = elves.copy()
    iterations += 1
    for i, elf in enumerate(elves):
        if len({(elf[0] - 1, elf[1]),
                (elf[0] - 1, elf[1] - 1),
                (elf[0], elf[1] - 1),
                (elf[0] + 1, elf[1] - 1),
                (elf[0] + 1, elf[1]),
                (elf[0] + 1, elf[1] + 1),
                (elf[0], elf[1] + 1),
                (elf[0] - 1, elf[1] + 1)}.intersection(set(elves))) != 0:
            for direction in order:
                if not elves_present(elf, direction):
                    proposed[i] = translate(elf, direction)
                    break
    for i in range(len(elves)):
        if proposed.count(proposed[i]) == 1:
            elves[i] = proposed[i]
    order.append(order[0])
    del order[0]
    proposed = elves.copy()
print(iterations)
