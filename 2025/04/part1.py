with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

rolls = set()


def get_roll_value(i, j):
    if i < 0 or i >= len(lines): return 0
    if j < 0 or j >= len(lines[0]): return 0
    return 1 if lines[i][j] == "@" else 0


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
            rolls.add((i, j))

print(len(rolls))