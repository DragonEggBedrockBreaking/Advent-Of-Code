import re
with open("data2.txt", "r") as f:
    lines = f.read().splitlines()
input = lines.pop()
input = re.findall(r"\d+|\D+", input)
lines.remove("")
grids = []
LIMIT = 3
grids.append([line[8:] for line in lines[:4]])
grids.append([line[:4] for line in lines[4:8]])
grids.append([line[4:8] for line in lines[4:8]])
grids.append([line[8:] for line in lines[4:8]])
grids.append([line[8:12] for line in lines[8:]])
grids.append([line[12:] for line in lines[8:]])
"""
grids.append([line[50:100] for line in lines[:50]])
grids.append([line[100:] for line in lines[:50]])
grids.append([line[50:100] for line in lines[50:100]])
grids.append([line[:50] for line in lines[100:150]])
grids.append([line[50:100] for line in lines[100:150]])
grids.append([line[:50] for line in lines[150:]])
"""
direction = 0
pos = [0, 0, 0]
connections = {
    (0, 0): (5, 0),
    (0, 1): (3, 3),
    (0, 2): (2, 3),
    (0, 3): (1, 3),
    (1, 0): (2, 2),
    (1, 1): (4, 1),
    (1, 2): (5, 1),
    (1, 3): (0, 3),
    (2, 0): (3, 2),
    (2, 1): (4, 2),
    (2, 2): (1, 0),
    (2, 3): (0, 2),
    (3, 0): (5, 3),
    (3, 1): (4, 3),
    (3, 2): (2, 0),
    (3, 3): (0, 1),
    (4, 0): (5, 2),
    (4, 1): (1, 1),
    (4, 2): (2, 1),
    (4, 3): (3, 1),
    (5, 0): (0, 0),
    (5, 1): (1, 2),
    (5, 2): (4, 0),
    (5, 3): (3, 0)
}
touching = ((0, 3), (1, 2), (2, 3), (3, 4), (4, 5))
"""
connections = {}
touching = ()
"""


def get_new_pos(face, x, y, direction):
    print(face, x, y, direction)
    newface, newside = connections[(face, direction)]
    print(newface, newside)
    match newside:
        case 0:
            if ((face, newface) not in touching) and ((newface, face) not in touching):
                x = y
            y = LIMIT
        case 1:
            if ((face, newface) not in touching) and ((newface, face) not in touching):
                y = x
            y = LIMIT
        case 2:
            if ((face, newface) not in touching) and ((newface, face) not in touching):
                x = y
            y = 0
        case 3:
            if ((face, newface) not in touching) and ((newface, face) not in touching):
                y = x
            x = 0
    direction = (newside + 2) % 4
    print(newface, x, y, direction)
    return ([newface, x, y], direction)


for char in input:
    print(pos, direction)
    if char.isnumeric():
        for i in range(int(char)):
            match direction:
                case 0:
                    if pos[2] == LIMIT:
                        newpos, newdir = get_new_pos(pos[0], pos[1], pos[2], direction)
                        if grids[newpos[0]][newpos[1]][newpos[2]] != "#":
                            pos, dir = newpos, newdir
                        continue
                    match grids[pos[0]][pos[1]][pos[2] + 1]:
                        case ".":
                            pos[2] += 1
                        case "#":
                            continue
                case 1:
                    if pos[1] == LIMIT:
                        newpos, newdir = get_new_pos(pos[0], pos[1], pos[2], direction)
                        if grids[newpos[0]][newpos[1]][newpos[2]] != "#":
                            pos, dir = newpos, newdir
                        continue

                    match grids[pos[0]][pos[1] + 1][pos[2]]:
                        case ".":
                            pos[1] += 1
                        case "#":
                            continue
                case 2:
                    if pos[2] == 0:
                        newpos, newdir = get_new_pos(pos[0], pos[1], pos[2], direction)
                        if grids[newpos[0]][newpos[1]][newpos[2]] != "#":
                            pos, dir = newpos, newdir
                        continue

                    match grids[pos[0]][pos[1]][pos[2] - 1]:
                        case ".":
                            pos[2] -= 1
                        case "#":
                            continue
                case 3:
                    if pos[1] == 0:
                        newpos, newdir = get_new_pos(pos[0], pos[1], pos[2], direction)
                        if grids[newpos[0]][newpos[1]][newpos[2]] != "#":
                            pos, dir = newpos, newdir
                        continue

                    match grids[pos[0]][pos[1] - 1][pos[2]]:
                        case ".":
                            pos[1] -= 1
                        case "#":
                            continue
    else:
        match char:
            case "R":
                direction = (direction + 1) % 4
            case "L":
                direction = (direction - 1) % 4

print(pos, direction)
