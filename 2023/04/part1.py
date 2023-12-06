with open("input.txt", "r", encoding="utf-8") as f:
    lines = [line.replace("  ", " ") for line in f.read().splitlines()]

total = 0
for line in lines:
    main = line.split(": ")[1]
    first = set(main.split(" | ")[0].split())
    second = set(main.split(" | ")[1].split())
    if first & second:
        total += 2**(len(first & second)-1)

print(total)
