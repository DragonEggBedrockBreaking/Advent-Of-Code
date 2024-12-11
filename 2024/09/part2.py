with open("input.txt", "r", encoding="utf8") as f:
    raw = list(int(v) for v in f.read().splitlines()[0])

structure = []
current = 0
for i, v in enumerate(raw):
    if i % 2:
        structure.append((".", v))
    else:
        structure.append((current, v))
        current += 1

current = float("inf")
while any(x[0] == "." for x in structure):
    if structure[-1][0] == ".":
        structure.pop()
        continue
    found = False
    for i, v in enumerate(structure):
        if i < len(structure) - 1 and v[0] == structure[i+1][0]:
            structure[i] = (v[0], v[1] + structure[i+1][1])
            del structure[i+1]
            found = True
            break
    if found:
        continue

    for i, val in reversed(tuple(enumerate(structure))):
        if val[0] == "." or val[0] >= current:
            continue
        for j, v2 in enumerate(structure):
            if j >= i:
                continue
            if v2[0] == ".":
                if v2[1] >= val[1]:
                    structure[j] = val
                    structure[i] = (".", val[1])
                    if v2[1] != val[1]:
                        structure.insert(j+1, (".", v2[1] - val[1]))
                    current = val[0]
                    break
        else:
            continue
        break
    else:
        break


expanded = []
for val in structure:
    for _ in range(val[1]):
        expanded.append(val[0])

total = 0
for i, item in enumerate(expanded):
    if item == ".":
        continue
    total += i * item

print(total)
