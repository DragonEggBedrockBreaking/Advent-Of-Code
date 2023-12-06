with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
total = 0
for line in lines:
    num = ""
    for char in line:
        if char.isnumeric():
            num += char
            break
    for char in reversed(line):
        if char.isnumeric():
            num += char
            break
    total += int(num)
print(total)