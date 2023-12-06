with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    colours = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }
    for game in line.split(": ")[1].split("; "):
        for colour in game.split(", "):
            colours[colour.split(" ")[1]] = max(colours[colour.split(" ")[1]], int(colour.split(" ")[0]))
    total += colours["red"] * colours["blue"] * colours["green"]

print(total)
