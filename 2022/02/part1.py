winners = {"X": "C", "Y": "A", "Z": "B"}
draws = {"X": "A", "Y": "B", "Z": "C"}
scores = {"X": 1, "Y": 2, "Z": 3}

with open("data.txt", "r") as f:
    lines = f.read().splitlines()

total = 0

for line in lines:
    parts = line.split(" ")
    if parts[1] == ' ':
        continue
    if parts[0] == winners[parts[1]]:
        total += 6
    elif parts[0] == draws[parts[1]]:
        total += 3
    total += scores[parts[1]]

print(total)
