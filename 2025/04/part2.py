with open("input.txt", "r", encoding="utf8") as f:
    lines = tuple(map(lambda s: list(s), f.read().splitlines()))

rolls = set()


def get_roll_value(i, j):
    if i < 0 or i >= len(lines): return 0
    if j < 0 or j >= len(lines[0]): return 0
    return 1 if lines[i][j] == "@" else 0

while True:
    current = set()
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if lines[i][j] == ".": continue
            count = sum((get_roll_value(i-1, j-1),
                         get_roll_value(i-1, j),
                         get_roll_value(i-1, j+1),
                         get_roll_value(i, j-1),
                         get_roll_value(i, j+1),
                         get_roll_value(i+1, j-1),
                         get_roll_value(i+1, j),
                         get_roll_value(i+1, j+1)))
            if count < 4:
                current.add((i, j))
    for i, j in current:
        lines[i][j] = "."
    if len(current) == 0: break
    rolls |= current

print(len(rolls))