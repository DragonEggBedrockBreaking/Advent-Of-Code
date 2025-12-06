with open("input.txt", "r", encoding="utf8") as f:
    lines = [x.split() for x in f.read().splitlines()]

final = 0
for i, operation in enumerate(lines[-1]):
    current = 0 if operation == "+" else 1
    for row in lines[:-1]:
        if operation == "+":
            current += int(row[i])
        else:
            current *= int(row[i])
    final += current
print(final)
