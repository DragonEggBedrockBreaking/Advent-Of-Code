with open("input.txt", "r", encoding="utf8") as f:
    lines = [(list(x.split()[0]), [int(i) for i in x.split()[1].split(",")]) for x in f.read().splitlines()]


total = 0


def verify(data, find):
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


def run(data, find):
    global total
    if "?" not in data:
        if verify(data, find):
            return
        return
    if verify(data, find):
        return
    data1 = data.copy()
    data1[data.index("?")] = "."
    run(data1, find)
    data2 = data.copy()
    data2[data.index("?")] = "#"
    run(data2, find)


full_total = 0
for d, f in lines:
    total = 0
    run(d, f)
    full_total += total

print(full_total)
