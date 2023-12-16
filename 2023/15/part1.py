with open("input.txt", "r", encoding="utf8") as f:
    line = f.read().splitlines()[0]

total = 0
for part in line.split(","):
    s = 0
    for char in part:
        s += ord(char)
        s *= 17
        s %= 256
    total += s

print(total)
