with open("data.txt", "r") as f:
    lines = f.read().splitlines()

score = 0

for line in lines:
    ranges = line.split(",")
    first = ranges[0].split("-")
    second = ranges[1].split("-")
    set1 = set(range(int(first[0]), int(first[1]) + 1))
    set2 = set(range(int(second[0]), int(second[1]) + 1))
    if len(set1.intersection(set2)) > 0:
        score += 1

print(score)
