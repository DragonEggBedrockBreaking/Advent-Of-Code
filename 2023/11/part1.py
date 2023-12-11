with open("input.txt") as f:
    lines = [list(x) for x in f.read().splitlines()]

cols = []
for i in range(len(lines[0])):
    if all(line[i] != "#" for line in lines):
        cols.append(i)

rows = []
for i, line in enumerate(lines):
    if "#" not in line:
        rows.append(i)

hashtags = []
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "#":
            hashtags.append((i, j))

distances = 0
for i, hsh in enumerate(hashtags):
    for j, tag in enumerate(hashtags):
        if i <= j:
            continue
        row_distance = abs(hsh[0] - tag[0])
        for row in rows:
            if hsh[0] < row < tag[0] or tag[0] < row < hsh[0]:
                row_distance += 1
        col_distance = abs(hsh[1] - tag[1])
        for col in cols:
            if hsh[1] < col < tag[1] or tag[1] < col < hsh[1]:
                col_distance += 1
        distances += row_distance + col_distance

print(distances)
