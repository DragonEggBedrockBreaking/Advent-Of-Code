with open("data2.txt", "r") as f:
    lines = [list(ln) for ln in f.read().splitlines()]

right, left, up, down, edge = [], [], [], [], []
for i, row in enumerate(lines):
    for j, point in enumerate(row):
        match point:
            case ">":
                right.append([i, j])
            case "<":
                left.append([i, j])
            case "^":
                up.append([i, j])
            case "v":
                down.append([i, j])
            case "#":
                edge.append([i, j])
minutes = 150


def run(pos, endpos, minimum):
    global minutes
    if tuple(pos) == endpos:
        if minimum < minutes:
            minutes = minimum
            return
    if minimum >= minutes:
        return
    minimum += 1
    for k in range(len(right)):
        right[k][1] += 1
        if right[k][1] == len(lines[0]) - 1:
            right[k][1] = 1
    for k in range(len(left)):
        left[k][1] -= 1
        if left[k][1] == 0:
            left[k][1] = len(lines[0]) - 2
    for k in range(len(up)):
        up[k][0] -= 1
        if up[k][0] == 0:
            up[k][0] = len(lines[0]) - 2
    for k in range(len(down)):
        down[k][0] += 1
        if down[k][0] == len(lines[0]) - 1:
            down[k][0] = 1
    gone = False
    if all((pt := [pos[0], pos[1] + 1]) not in ls for ls in [right, left, up, down, edge]):
        run(pt, endpos, minimum)
        gone = True
    if all((pt := [pos[0] + 1, pos[1]]) not in ls for ls in [right, left, up, down, edge]):
        run(pt, endpos, minimum)
        gone = True
    if all((pt := [pos[0], pos[1] - 1]) not in ls for ls in [right, left, up, down, edge]):
        run(pt, endpos, minimum)
        gone = True
    if (pos[0] > 0) and (all((pt := [pos[0] - 1, pos[1]]) not in ls for ls in [right, left, up, down, edge])):
        run(pt, endpos, minimum)
        gone = True
    if (not gone) and (all(pos not in ls for ls in [right, left, up, down])):
        run(pos.copy(), endpos, minimum)
        gone = True
    if not gone:
        return


run([0, 1], (len(lines) - 1, len(lines[0]) - 2), 0)
print(minutes)
