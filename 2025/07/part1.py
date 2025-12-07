import functools

with open("input.txt", "r", encoding="utf8") as f:
    lines = [list(x) for x in f.read().splitlines()]
startx = lines[0].index("S")
lines = list(map(list, zip(*lines)))


@functools.cache
def go(x, y):
    if y == len(lines) - 1:
        return
    elif lines[x][y+1] == "|":
        return
    elif lines[x][y+1] == ".":
        lines[x][y+1] = "|"
        go(x, y+1)
    elif lines[x][y+1] == "^":
        if x > 0:
            lines[x-1][y+1] = "|"
            go(x-1, y+1)
        if x < len(lines) - 1:
            lines[x+1][y+1] = "|"
            go(x+1, y+1)


go(startx, 0)

lines = list(map(list, zip(*lines)))

count = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "^" and lines[i-1][j] == "|":
            count += 1

print(count)
