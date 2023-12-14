with open("input.txt", "r", encoding="utf-8") as f:
    lines = [list(line) for line in f.read().splitlines()]

def apply():
    global lines
    for k, line in enumerate(lines):
        rocks = [i for i, char in enumerate(line) if char == "O"]
        for rock in rocks:
            for j in range(rock - 1, -1, -1):
                if lines[k][j] in "#O":
                    lines[k][rock], lines[k][j + 1] = lines[k][j + 1], lines[k][rock]
                    break
            else:
                lines[k][rock], lines[k][0] = lines[k][0], lines[k][rock]

repetition = 0
lists = []
while True:
    lines = [list(line) for line in zip(*lines)]
    apply()
    lines = [list(line) for line in zip(*lines)]
    apply()
    lines = [list(line) for line in zip(*list(reversed(lines)))]
    apply()
    lines = [list(reversed(line)) for line in reversed([list(line) for line in zip(*lines)])]
    apply()
    lines = [list(reversed(line)) for line in lines]
    if lines in lists:
        repetition = lists.index(lines)
        break
    lists.append(lines)

for i in range((1000000000 - len(lists) - 1) % (len(lists) - repetition)):
    lines = [list(line) for line in zip(*lines)]
    apply()
    lines = [list(line) for line in zip(*lines)]
    apply()
    lines = [list(line) for line in zip(*list(reversed(lines)))]
    apply()
    lines = [list(reversed(line)) for line in reversed([list(line) for line in zip(*lines)])]
    apply()
    lines = [list(reversed(line)) for line in lines]

total = 0
for i, line in enumerate(reversed(lines)):
    total += (i+1) * line.count("O")
print(total)
