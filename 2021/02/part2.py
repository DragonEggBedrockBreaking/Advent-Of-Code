with open('data.txt', 'r', encoding="utf-8") as f: data = f.read().splitlines()  # Gets input from data.txt
horizontal, depth, aim = 0, 0, 0
for line in data:
    line_part = line.split(" ")[1]
    match line.split(" ")[0]:
        case "forward": horizontal, depth = horizontal + int(line_part), depth + int(line_part) * aim
        case "down": aim += int(line_part)
        case "up": aim -= int(line_part)
print(horizontal * depth)
