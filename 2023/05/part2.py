with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

seeds = [int(i) for i in lines[0].split()[1:]]
maps = [[tuple([int(j) for j in i.split()]) for i in m.splitlines()[1:]] for m in "\n".join(lines[2:]).split("\n\n")]

i = 0
solution_seed = 0
while True:
    i += 1
    print(i)
    seed = i
    for m in reversed(maps):
        for group in m:
            if seed in range(group[0], group[0]+group[2]):
                seed = group[1]+(seed-group[0])
                break
    for j in range(len(seeds)//2):
        if seed in range(seeds[2*j], seeds[2*j]+seeds[2*j+1]):
            solution_seed = i
            break
    if solution_seed != 0:
        break

print(solution_seed)
