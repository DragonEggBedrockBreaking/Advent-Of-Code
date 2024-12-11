with open("input.txt", "r", encoding="utf8") as f:
    lines = {int(x.split(": ")[0]): [int(y) for y in x.split(": ")[1].split()] for x in f.read().splitlines()}


def test(target, values, operators, index=0):
    if index == len(values) - 1:
        total = values[0]
        for i, value in enumerate(values):
            if i == len(values) - 1:
                continue
            if operators[i] == "+":
                total += values[i+1]
            elif operators[i] == "x":
                total *= values[i+1]
        return total == target
    operators1 = operators.copy()
    operators1[index] = "+"
    if test(target, values, operators1, index+1):
        return True
    operators2 = operators.copy()
    operators2[index] = "x"
    return test(target, values, operators2, index+1)


s = 0
for key, val in lines.items():
    if test(key, val, ["" for _ in range(len(val))]):
        s += key

print(s)
