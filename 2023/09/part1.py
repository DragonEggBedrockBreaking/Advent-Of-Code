with open("input.txt", "r", encoding="utf8") as f:
    lines = [[[int(i) for i in x.split()]] for x in f.read().splitlines()]

total = 0
for i in range(len(lines)):
    while len(set(lines[i][-1])) > 1:
        lines[i].append([lines[i][-1][x+1] - lines[i][-1][x] for x in range(len(lines[i][-1])-1)])
    for j in range(len(lines[i])-2, -1, -1):
        lines[i][j].append(lines[i][j+1][-1] + lines[i][j][-1])
    total += lines[i][0][-1]

print(total)
