with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

count = 0
length_individual = len(lines[0])
length_total = len(lines)
for i, line in enumerate(lines):
    if i < length_total - 2:
        for j, char in enumerate(line):
            if j < length_individual - 2:
                if (char == "M" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "S") or (char == "S" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "M"):
                    if (lines[i][j+2] == "M" and lines[i+2][j] == "S") or (lines[i][j+2] == "S" and lines[i+2][j] == "M"):
                        count += 1

print(count)
