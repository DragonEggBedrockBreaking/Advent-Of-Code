with open("input.txt", "r", encoding="utf-8") as f:
    lines = [line.replace("  ", " ") for line in f.read().splitlines()]

card_copies = {}
for i in range(len(lines)):
    card_copies[i+1] = 1

for i, line in enumerate(lines):
    main = line.split(": ")[1]
    first = set(main.split(" | ")[0].split())
    second = set(main.split(" | ")[1].split())
    matching = len(first & second)
    for j in range(matching):
        if i+j+2 in card_copies.keys():
            card_copies[i+j+2] += card_copies[i+1]

print(sum(card_copies.values()))
