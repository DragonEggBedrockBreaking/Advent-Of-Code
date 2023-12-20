from math import lcm

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()
    main_data = {line.split(" -> ")[0][1:]: line.split(" -> ")[1].split(", ") for line in lines}
    type_data = {line.split(" -> ")[0][1:]: line.split(" -> ")[0][0] for line in lines}
    charges = {line.split(" -> ")[0][1:]: {"overall": False} for line in lines if "%" in line}
for k1, v1 in type_data.items():
    if v1 != "&":
        continue
    for k2, v2 in main_data.items():
        if k1 in v2:
            if k1 not in charges:
                charges[k1] = {k2: False}
            else:
                charges[k1][k2] = False

def pulse(current, pulse_type):
    for output in main_data[current]:
        if output not in type_data:
            continue
        match type_data[output]:
            case "%":
                if pulse_type == "low":
                    if charges[output]["overall"]:
                        charges[output]["overall"] = False
                        queue.append((output, "low"))
                    else:
                        charges[output]["overall"] = True
                        queue.append((output, "high"))
            case "&":
                charges[output][current] = pulse_type == "high"
                if all(charge for charge in charges[output].values()):
                    queue.append((output, "low"))
                else:
                    queue.append((output, "high"))


master = ""
for key, value in main_data.items():
    if "rx" in value:
        master = key
        break
master_searches = []
for key, value in main_data.items():
    if master in value:
        master_searches.append(key)

nums = [0, 0, 0, 0]
count = 0
while any(not num for num in nums):
    count += 1
    queue = [("roadcaster", "low")]
    while queue:
        if (search := queue[0][0]) in master_searches and queue[0][1] == "high":
            nums[master_searches.index(search)] = count
        pulse(*queue.pop(0))
print(lcm(*nums))
