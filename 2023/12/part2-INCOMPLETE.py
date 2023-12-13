import functools

with open("input.txt", "r", encoding="utf8") as f:
    lines = [[list(x.split()[0]), [int(i) for i in x.split()[1].split(",")]] for x in f.read().splitlines()]
for i, line in enumerate(lines):
    lines[i][0] = 5 * line[0]
    lines[i][1] = 5 * line[1]


total = 0


@functools.cache
def verify(data, find):
    data = list(data)
    find = list(find)
    last_char = ""
    global total
    find = find.copy()
    count = 0
    for char in data:
        match char:
            case "." | "?":
                if len(find) != 0 and count == find[0]:
                    find = find[1:]
                elif last_char == "#":
                    return False
                last_char = "."
                count = 0
            case "#":
                if len(find) == 0:
                    return False
                last_char = "#"
                count += 1
                if count > find[0]:
                    return False
    if len(find) > 0 and count == find[0]:
        find = find[1:]
    if len(find) == 0:
        total += 1
        return True
    return False


@functools.cache
def run(data, find):
    global total
    if "?" not in data:
        if verify(data, find):
            return
        return
    if verify(data, find):
        return
    data1 = list(data)
    data1[data.index("?")] = "."
    run(tuple(data1), find)
    data2 = list(data)
    data2[data.index("?")] = "#"
    run(tuple(data2), find)


full_total = 0
for i, v in enumerate(lines):
    print(i)
    total = 0
    run(tuple(v[0]), tuple(v[1]))
    full_total += total

print(full_total)
