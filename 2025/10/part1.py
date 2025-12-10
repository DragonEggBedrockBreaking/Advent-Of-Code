import collections
import z3

with open("input.txt") as f:
    lines = [line.split() for line in f.read().splitlines()]

indicators = tuple(line.pop(0)[1:-1] for line in lines)
joltage = tuple(tuple(map(int, line.pop()[1:-1].split(","))) for line in lines)
button_tuples = tuple(tuple(tuple(map(int, nums[1:-1].split(","))) for nums in line) for line in lines)

total = 0
for i, indicator in enumerate(indicators):
    buttons = button_tuples[i]
    button_data = collections.defaultdict(list)
    for j, button in enumerate(buttons):
        for effect in button:
            button_data[effect].append(j)
    z3_vars = [z3.Int(f"x{j}") for j in range(len(buttons))]
    opt = z3.Optimize()
    for var in z3_vars:
        opt.add(var >= 0)
    for effect, js in button_data.items():
        wanted = 0 if indicator[effect] == "." else 1
        opt.add(sum(z3_vars[j] for j in js) % 2 == wanted)
    f = sum(z3_vars)
    opt.minimize(sum(z3_vars))
    opt.check()
    total += int(str(opt.model().evaluate(f)))

print(total)
