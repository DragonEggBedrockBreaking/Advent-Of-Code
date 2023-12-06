with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

total = 0
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
            good = False
            surroundings = []
            if index > 0:
                surroundings.append(line[index-1])
                if i > 0:
                    surroundings.append(lines[i-1][index-1])
                if i < len(lines)-1:
                    surroundings.append(lines[i+1][index-1])
            if index < len(line)-1:
                surroundings.append(line[index+1])
                if i > 0:
                    surroundings.append(lines[i-1][index+1])
                if i < len(lines)-1:
                    surroundings.append(lines[i+1][index+1])
            if i > 0:
                surroundings.append(lines[i-1][index])
            if i < len(lines)-1:
                surroundings.append(lines[i+1][index])
            for surrounding in surroundings:
                if surrounding != "." and not surrounding.isnumeric():
                    good = True
                    break
            if good:
                break
        else:
            continue
        total += int(num)

print(total)