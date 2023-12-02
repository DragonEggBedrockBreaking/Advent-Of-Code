with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    id = int(line.split(": ")[0].split(" ")[1])
    for game in line.split(": ")[1].split("; "):
        colours = {
            "red": 0,
            "blue": 0,
            "green": 0
        }
        for section in game.split(", "):
            colours[section.split(" ")[1]] = int(section.split(" ")[0])
        if colours["red"] > 12 or colours["blue"] > 14 or colours["green"] > 13:
            break
    else:
        total += id

print(total)