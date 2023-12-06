winning = {"A": "P", "B": "S", "C": "R"}
drawing = {"A": "R", "B": "P", "C": "S"}
losing = {"A": "S", "B": "R", "C": "P"}
scores = {"R": 1, "P": 2, "S": 3}

with open("data.txt", "r") as f:
    lines = f.read().splitlines()

total = 0

for line in lines:
    parts = line.split(" ")
    if parts[1] == "X":
        choice = losing[parts[0]]
    elif parts[1] == "Y":
        choice = drawing[parts[0]]
        total += 3
    else:
        choice = winning[parts[0]]
        total += 6
    total += scores[choice]

print(total)
