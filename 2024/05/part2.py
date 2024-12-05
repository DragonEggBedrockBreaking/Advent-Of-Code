ordering_rules = {}
production = []

with open("input.txt", "r", encoding="utf8") as f:
    first = True
    for line in f:
        if line.strip() == "":
            first = False
        elif first:
            one, two = line.strip().split("|")
            if two in ordering_rules.keys():
                ordering_rules[two].add(one)
            else:
                ordering_rules[two] = {one}
        else:
            production.append(line.strip().split(","))

total = 0
for line in production:
    broken = False
    for i, val in enumerate(line):
        if val in ordering_rules.keys() and len(set(line[i+1:]) & ordering_rules[val]) != 0:
            broken = True
            break
    if broken:
        newline = [None, None]
        for val in line:
            if val not in ordering_rules.keys():
                newline.insert(0, val)
            else:
                for i, val2 in enumerate(newline):
                    if len(set(newline[i+1:]) & ordering_rules[val]) == 0:
                        newline.insert(i+1, val)
                        break
        newline.remove(None)
        newline.remove(None)
        total += int(newline[len(newline) // 2])

print(total)
