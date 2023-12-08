with open("input.txt") as f:
    lines = [line.replace(")", "") for line in f.read().splitlines()]

progression = lines[0]
data = {x.split(" =")[0]: tuple(x.split("(")[1].split(", ")) for x in lines[2:]}
current, i = "AAA", 0
while current != "ZZZ":
    current = data[current][0 if progression[0] == "L" else 1]
    progression = progression[1:] + progression[0]
    i += 1
print(i)
