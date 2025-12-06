from math import prod

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
    items = ["".join([x[j] for x in secs if x[j].isnumeric()]) for j in range(len(secs[0])-1, -1, -1)]
    nums = [int(x) for x in items if x.isnumeric()]
    return sum(nums) if operation == "+" else prod(nums)


it, total = 0, 0
for i, (op, count) in enumerate(ops_data):
    if i == len(ops_data) - 1:
        sections = [x[it:] for x in lines]
    else:
        sections = [x[it:it+count] for x in lines]
    it += count + 1
    total += calc(sections, op)

print(total)
