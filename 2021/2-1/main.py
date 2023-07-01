with open('data.txt', 'r', encoding="utf-8") as f: data = f.read().splitlines()  # Gets input from data.txt
horizontal, depth = 0, 0
for line in data:
    match line.split(" ")[1]:
        case "forward": horizontal += int(line.split(" ")[1])
        case "down": depth += int(line.split(" ")[1])
        case "up": depth -= int(line.split(" ")[1])
print(horizontal * depth)
