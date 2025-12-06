from math import prod

with open("input.txt", "r", encoding="utf8") as f:
    lines = [x.split() for x in f.read().splitlines()]

final = 0
for i, operation in enumerate(lines[-1]):
    nums = tuple(map(int, [row[i] for row in lines[:-1]]))
    final += sum(nums) if operation == "+" else prod(nums)

print(final)
