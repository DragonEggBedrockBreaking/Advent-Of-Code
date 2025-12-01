with open("input.txt", "r") as f:
    lines = f.read().splitlines()
count, current = 0, 50
for line in lines:
    num = int(line[1:])
    current += num * (1 if line[0] == "R" else -1)
    current %= 100
    if current == 0:
        count += 1
print(count)