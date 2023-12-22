import copy

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

data = {}
for i, line in enumerate(lines):
    first, second = tuple(map(int, line.split("~")[0].split(","))), tuple(map(int, line.split("~")[1].split(",")))
    blocks = []
    if first[0] != second[0]:
        for j in range(first[0], second[0] + 1):
            blocks.append([j, first[1], first[2]])
    elif first[1] != second[1]:
        for j in range(first[1], second[1] + 1):
            blocks.append([first[0], j, first[2]])
    elif first[2] != second[2]:
        for j in range(first[2], second[2] + 1):
            blocks.append([first[0], first[1], j])
    else:
        blocks.append(list(first))
    data[i] = blocks
data = dict(sorted(data.items(), key=lambda x: x[1][0][2]))


def fall(dictionary, breakout=False):
    j = 0
    for key in dictionary.keys():
        j += 1
        if not breakout:
            print(j)
        value = dictionary[key]
        if any(v[2] == 1 for v in value):
            continue
        drop_level = 0
        for i in range(min(v[2] for v in value) - 1, 0, -1):
            blocked = False
            top_points = set((x[0], x[1]) for x in value)
            for k1, v1 in dictionary.items():
                if k1 == key or all(v2[2] != i for v2 in v1):
                    continue
                bottom_points = set((x[0], x[1]) for x in v1)
                if len(bottom_points & top_points) > 0:
                    blocked = True
                    break
            if blocked:
                break
            drop_level += 1
        for i in range(len(value)):
            dictionary[key][i][2] -= drop_level
    return dictionary


j = 0
data = fall(data)
can_be_disintegrated = 0
for k, v in data.items():
    j += 1
    print(j)
    new_data = copy.deepcopy(data)
    del new_data[k]
    new_new_data = fall(copy.deepcopy(new_data), True)
    can_be_disintegrated += len(set(tuple([tuple([tuple(x) for x in v]) for v in new_new_data.values()])) - (set(tuple([tuple([tuple(x) for x in v]) for v in new_data.values()])) & set(tuple([tuple([tuple(x) for x in v]) for v in new_new_data.values()]))))
print(can_be_disintegrated)
