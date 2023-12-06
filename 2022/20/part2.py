from copy import deepcopy

KEY = 811589153

with open("data.txt", "r") as f:
    lines = [f"{int(v) * KEY}_{i}" for i, v in enumerate(f.read().splitlines())]
reference = deepcopy(lines)


def shuffle():
    for val in reference:
        index = lines.index(val)
        move = int(val.split("_")[0])
        #if move > 0:
        move %= (len(lines) - 1)
        #else:
            #move = -(-move % (len(lines) - 1))
        if move == 0:
            pass
        elif index + move == 0:
            move -= 1
        elif index + move >= len(lines):
            move -= len(lines) - 1
        del lines[index]
        if index + move == -1:
            lines.append(val)
        else:
            lines.insert(index + move, val)


for _ in range(10):
    shuffle()

for i, v in enumerate(lines):
    lines[i] = v.split("_")[0]

i = lines.index("0")
print(int(lines[((1000 + i) %
                 len(lines))]) + int(lines[((2000 + i) %
                                            len(lines))]) + int(lines[((3000 + i) %
                                                                       len(lines))]))
