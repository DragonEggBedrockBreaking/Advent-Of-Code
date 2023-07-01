with open("data.txt", "r") as f:
    lines = f.read().splitlines()

NUM_LINES = len(lines) - 1
LEN_LINES = len(lines[0]) - 1
scores = []

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if (i == 0) or (i == NUM_LINES) or (j == 0) or (j == LEN_LINES):
            continue

        left, right, up, down = 0, 0, 0, 0

        for ind in range(j - 1, -1, -1):
            left += 1
            if int(line[ind]) >= int(char):
                break

        for ind in range(j + 1, len(line)):
            right += 1
            if int(line[ind]) >= int(char):
                break

        for ind in range(i - 1, -1, -1):
            up += 1
            if int(lines[ind][j]) >= int(char):
                break

        for ind in range(i + 1, len(lines)):
            down += 1
            if int(lines[ind][j]) >= int(char):
                break

        scores.append(left * right * up * down)

print(max(scores))
