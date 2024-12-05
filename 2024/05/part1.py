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
    for i, val in enumerate(line):
        if val in ordering_rules.keys() and len(set(line[i+1:]) & ordering_rules[val]) != 0:
            break
    else:
        total += int(line[len(line) // 2])

print(total)
