with open("data.txt", "r") as f:
    lines = f.read().splitlines()

x, i = 1, 0

total = 0

for line in lines:
    i += 1
    if (i + 20) % 40 == 0:
        total += i * x
    if "addx" in line:
        i += 1
        if (i + 20) % 40 == 0:
            total += i * x
        x += int(line.split()[1])

print(total)
