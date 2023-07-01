with open("data.txt", "r") as f:
    lines = f.read().splitlines()

NUM = 8

monkeys = [[] for _ in range(NUM)]
inspections = [0 for _ in range(NUM)]
monkey_data = {}

for i in range(NUM):
    for item in lines[i * 7 + 1].split(": ")[1].split(", "):
        monkeys[i].append(int(item))

    monkey_data[str(i) + "_operation"] = lines[i * 7 + 2].split("= ")[1]
    monkey_data[str(i) + "_test"] = int(lines[i * 7 + 3].split("by ")[1])
    monkey_data[str(i) + "_true"] = int(lines[i * 7 + 4].split("monkey ")[1])
    monkey_data[str(i) + "_false"] = int(lines[i * 7 + 5].split("monkey ")[1])

for _ in range(20):
    for i, monkey in enumerate(monkeys):
        while len(monkeys[i]) > 0:
            inspections[i] += 1

            item = monkeys[i][0]

            operation = monkey_data[str(i) + "_operation"]
            if operation == "old * old":
                item **= 2
            elif "*" in operation:
                item *= int(operation.split(" ")[2])
            elif "+" in operation:
                item += int(operation.split(" ")[2])
            else:
                print(operation)

            item //= 3

            if item % monkey_data[str(i) + "_test"] == 0:
                monkeys[monkey_data[str(i) + "_true"]].append(item)
            else:
                monkeys[monkey_data[str(i) + "_false"]].append(item)

            del monkeys[i][0]

maximum = max(inspections)
inspections.remove(maximum)
print(maximum * max(inspections))
