with open("input.txt", "r", encoding="utf-8") as f:
    lines = [list(line) for line in f.read().splitlines()]

lines = [list(line) for line in zip(*lines)]
for k, line in enumerate(lines):
    rocks = [i for i, char in enumerate(line) if char == "O"]
    for rock in rocks:
        for j in range(rock - 1, -1, -1):
            if lines[k][j] in "#O":
                lines[k][rock], lines[k][j + 1] = lines[k][j + 1], lines[k][rock]
                break
        else:
            lines[k][rock], lines[k][0] = lines[k][0], lines[k][rock]


lines = [list(line) for line in zip(*lines)]
total = 0
for i, line in enumerate(reversed(lines)):
    total += (i+1) * line.count("O")
print(total)
