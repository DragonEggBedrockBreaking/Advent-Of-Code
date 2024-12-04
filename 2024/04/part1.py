with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

count = 0
length_individual = len(lines[0])
length_total = len(lines)
for line in lines:
    count += line.count("XMAS")
    count += line.count("SAMX")
for i, line in enumerate(lines):
    if i < length_total - 3:
        for j, char in enumerate(line):
            if j < length_individual - 3:
                if char == "X" and lines[i+1][j+1] == "M" and lines[i+2][j+2] == "A" and lines[i+3][j+3] == "S":
                    count += 1
                if char == "S" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "M" and lines[i+3][j+3] == "X":
                    count += 1
            if j > 2:
                if char == "X" and lines[i+1][j-1] == "M" and lines[i+2][j-2] == "A" and lines[i+3][j-3] == "S":
                    count += 1
                if char == "S" and lines[i+1][j-1] == "A" and lines[i+2][j-2] == "M" and lines[i+3][j-3] == "X":
                    count += 1
            if char == "X" and lines[i+1][j] == "M" and lines[i+2][j] == "A" and lines[i+3][j] == "S":
                count += 1
            if char == "S" and lines[i+1][j] == "A" and lines[i+2][j] == "M" and lines[i+3][j] == "X":
                count += 1

print(count)
