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
    global lruns, hruns
    outputs = main_data[current]
    match pulse_type:
        case "low":
            lruns += len(outputs)
        case "high":
            hruns += len(outputs)
    for output in outputs:
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


lruns, hruns = 0, 0
for _ in range(1000):
    lruns += 1
    queue = [("roadcaster", "low")]
    while queue:
        pulse(*queue.pop(0))
print(lruns * hruns)
