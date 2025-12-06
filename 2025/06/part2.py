with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()
ops = lines.pop()
ops_data = []
for char in ops:
    if char in ("+", "*"):
        ops_data.append([char, 0])
    else:
        ops_data[-1][1] += 1


def calc(secs, operation):
    items = []
    for j in range(len(secs[0])-1, -1, -1):
        items.append("".join([x[j] for x in secs if x[j].isnumeric()]))
    items = [int(x) for x in items if x.isnumeric()]
    final = 0 if operation == "+" else 1
    for item in items:
        if operation == "+":
            final += int(item)
        else:
            final *= int(item)
    return final


it, total = 0, 0
for i, (op, count) in enumerate(ops_data):
    if i < len(ops_data) - 1:
        sections = [x[it:it+count] for x in lines]
        it += count + 1
        total += calc(sections, op)
    else:
        sections = [x[it:] for x in lines]
        total += calc(sections, op)
        break

print(total)
