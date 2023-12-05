with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

seeds = [int(i) for i in lines[0].split()[1:]]
maps = [[tuple([int(j) for j in i.split()]) for i in m.splitlines()[1:]] for m in "\n".join(lines[2:]).split("\n\n")]

for i in range(len(seeds)):
    for m in maps:
        for group in m:
            if seeds[i] in range(group[1], group[1]+group[2]):
                seeds[i] = group[0]+(seeds[i]-group[1])
                break

print(min(seeds))


