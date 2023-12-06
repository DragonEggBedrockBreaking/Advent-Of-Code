with open("data.txt", "r") as f:
    lines = f.read().splitlines()

total = len(lines) * 2 + (len(lines[0]) - 2) * 2

NUM_LINES = len(lines) - 1
LEN_LINES = len(lines[0]) - 1
increment = False

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if (i == 0) or (i == NUM_LINES) or (j == 0) or (j == LEN_LINES):
            continue

        for ind in range(0, j):
            if int(line[ind]) >= int(char):
                break
        else:
            increment = True

        for ind in range(j + 1, len(line)):
            if int(line[ind]) >= int(char):
                break
        else:
            increment = True

        for ind in range(0, i):
            if int(lines[ind][j]) >= int(char):
                break
        else:
            increment = True

        for ind in range(i + 1, len(lines)):
            if int(lines[ind][j]) >= int(char):
                break
        else:
            increment = True

        if increment:
            total += 1

        increment = False

print(total)
