with open("input.txt", "r") as f:
    lines = f.read().splitlines()
count, current = 0, 50
for line in lines:
    num = int(line[1:])
    inc = 1 if line[0] == "R" else -1
    for _ in range(num):
        current += inc
        current %= 100
        if current == 0:
            count += 1
print(count)