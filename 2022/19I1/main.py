from copy import deepcopy
from functools import lru_cache

with open("data.txt", "r") as f:
    blueprints = [
        ((int(
            line.split()[6]), int(
            line.split()[12]), int(
                line.split()[18]), int(
                    line.split()[21]), int(
                        line.split()[27]), int(
                            line.split()[30]))) for line in f.read().splitlines()]

geodes = set()
blueprint_counts = []


@lru_cache(maxsize=2**23)
def optimise(resources, robots, i, recipe):
    if i == 24:
        geodes.add(resources[3])
        return
    i += 1
    made = [False, False, False, False]
    if (resources[0] >= recipe[4]) and (resources[2] >= recipe[5]):
        made[3] = True
    else:
        if (resources[0] >= recipe[0]) and (i < 21) and (robots.count("ore") < max(recipe[0], recipe[1], recipe[2], recipe[4])):
            made[0] = True
        if (resources[0] >= recipe[1]) and (i < 19) and (robots.count("clay") < recipe[3]):
            made[1] = True
        if (resources[0] >= recipe[2]) and (resources[1] >= recipe[3]) and (
                i < 21) and (robots.count("obsidian") < recipe[5]):
            made[2] = True
    resources = list(resources)
    resources[0] += robots.count("ore")
    resources[1] += robots.count("clay")
    resources[2] += robots.count("obsidian")
    resources[3] += robots.count("geode")
    resources = tuple(resources)
    if made[3]:
        res = list(deepcopy(resources))
        bots = list(deepcopy(robots))
        res[0] -= recipe[4]
        res[2] -= recipe[5]
        bots.append("geode")
        optimise(tuple(res), tuple(bots), i, recipe)
    else:
        optimise(deepcopy(resources), deepcopy(robots), i, recipe)
        if made[0]:
            res = list(deepcopy(resources))
            bots = list(deepcopy(robots))
            res[0] -= recipe[0]
            bots.append("ore")
            optimise(tuple(res), tuple(bots), i, recipe)
        if made[1]:
            res = list(deepcopy(resources))
            bots = list(deepcopy(robots))
            res[0] -= recipe[1]
            bots.append("clay")
            optimise(tuple(res), tuple(bots), i, recipe)
        if made[2]:
            res = list(deepcopy(resources))
            bots = list(deepcopy(robots))
            res[0] -= recipe[2]
            res[1] -= recipe[3]
            bots.append("obsidian")
            optimise(tuple(res), tuple(bots), i, recipe)


for i, blueprint in enumerate(blueprints):
    print(i + 1)
    optimise((0, 0, 0, 0), tuple(["ore"]), 0, blueprint)
    print(max(geodes))
    blueprint_counts.append(max(geodes) * (i + 1))
    geodes = set()

print(sum(blueprint_counts))
