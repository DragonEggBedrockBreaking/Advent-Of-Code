with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()
grids = [[] for _ in range(lines.count("") + 1)]
find = 0
for line in lines:
    if line == "":
        find += 1
        continue
    grids[find].append(line)

total = 0
for grid in grids:
    for i in range(1, len(grid)):
        left, right = grid[:i], grid[i:]
        minimum = min(len(left), len(right))
        if left[-minimum:] == list(reversed(right[:minimum])):
            total += len(left) * 100
            break
    else:
        for j in range(1, len(grid[0])):
            transpose = [''.join(row) for row in zip(*grid)]
            top, bottom = transpose[:j], transpose[j:]
            minimum = min(len(top), len(bottom))
            if top[-minimum:] == list(reversed(bottom[:minimum])):
                total += len(top)
                break

print(total)
