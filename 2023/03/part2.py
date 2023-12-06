with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

numbers = {}
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if not char.isnumeric() or (j > 0 and line[j-1].isnumeric()):
            continue
        num = ""
        indices = []
        k = j
        while k < len(line) and line[k].isnumeric():
            num += line[k]
            indices.append(k)
            k += 1
        for index in indices:
            numbers[(i, index)] = num

total = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char != "*":
            continue
        surroundings = set()
        for k in range(-1, 2):
            for l in range(-1, 2):
                if k == 0 and l == 0:
                    continue
                if (i+k, j+l) in numbers:
                    surroundings.add(int(numbers[(i+k, j+l)]))
        surroundings = list(surroundings)
        if len(surroundings) == 2:
            total += surroundings[0] * surroundings[1]

print(total)
