import numpy as np

with open("data.txt", "r") as f:
    lines = f.read().splitlines()

section = 1

crates = []
operations = []

for line in lines:
    if line == "":
        section += 1
        continue
    if section == 1:
        if "1" not in line:
            line += "                             "
            crates.append([line[i * 4 + 1] for i in range(9)])
    else:
        parts = line.split(" ")
        operations.append((int(parts[1]), int(parts[3]), int(parts[5])))

crates = np.array(crates)
crates = np.transpose(crates)
crates = crates.tolist()
crates = [i[::-1] for i in crates]
for i in range(9):
    while " " in crates[i]:
        crates[i].remove(" ")

for item in operations:
    for i in range(item[0]):
        crates[item[2] - 1].append(crates[item[1] - 1][i - item[0]])
    for i in range(item[0]):
        crates[item[1] - 1].pop()

print("".join([i[-1] for i in crates]))
