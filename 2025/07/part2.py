import functools

with open("input.txt", "r", encoding="utf8") as f:
    lines = [list(x) for x in f.read().splitlines()]
startx = lines[0].index("S")
lines = list(map(list, zip(*lines)))


@functools.cache
def go(x, y):
    if y == len(lines) - 1:
        return 1
    elif lines[x][y+1] == "|":
        return go(x, y+1)
    elif lines[x][y+1] == ".":
        lines[x][y+1] = "|"
        return go(x, y+1)
    elif lines[x][y+1] == "^":
        splits = 0
        if x > 0:
            lines[x-1][y+1] = "|"
            splits += go(x-1, y+1)
        if x < len(lines) - 1:
            lines[x+1][y+1] = "|"
            splits += go(x+1, y+1)
        return splits


print(go(startx, 0))
