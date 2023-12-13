from nltk.metrics.distance import edit_distance

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
        diffs = 0
        for k, ln in enumerate(left[-minimum:]):
            if len(right[:minimum]) <= k:
                break
            diffs += edit_distance(ln, list(reversed(right[:minimum]))[k])
        if diffs == 1:
            total += len(left) * 100
            break
    else:
        for j in range(1, len(grid[0])):
            transpose = [''.join(row) for row in zip(*grid)]
            top, bottom = transpose[:j], transpose[j:]
            minimum = min(len(top), len(bottom))
            diffs = 0
            for k, ln in enumerate(top[-minimum:]):
                if len(bottom[:minimum]) <= k:
                    break
                diffs += edit_distance(ln, list(reversed(bottom[:minimum]))[k])
            if diffs == 1:
                total += len(top)
                break

print(total)
