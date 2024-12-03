with open("input.txt", "r", encoding="utf8") as f:
    lines = [[int(y) for y in x.split()] for x in f.read().splitlines()]

count = 0
for line in lines:
    increase = 1 if line[0] < line[1] else -1
    for i in range(len(line) - 1):
        if (line[i+1] - line[i]) * increase not in (1, 2, 3):
            break
    else:
        count += 1

print(count)
