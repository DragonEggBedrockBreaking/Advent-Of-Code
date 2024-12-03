with open("input.txt", "r", encoding="utf8") as f:
    lines = [[int(y) for y in x.split()] for x in f.read().splitlines()]


def is_safe(l):
    increase = 1 if l[0] < l[1] else -1
    for i in range(len(l) - 1):
        if (l[i + 1] - l[i]) * increase not in (1, 2, 3):
            return False
    return True


count = 0
for line in lines:
    if is_safe(line):
        count += 1
    else:
        for j in range(len(line)):
            newline = line.copy()
            del newline[j]
            if is_safe(newline):
                count += 1
                break

print(count)
