import ast

with open("data.txt", "r") as f:
    lines = f.read().splitlines()

while "" in lines:
    lines.remove("")


def compareItems(first, second):
    if (type(first), type(second)) == (int, int):
        if first < second:
            return 1
        elif second < first:
            return -1
        else:
            return 0
    elif (type(first), type(second)) == (list, int):
        return compareItems(first, [second])
    elif (type(first), type(second)) == (int, list):
        return compareItems([first], second)
    elif (type(first), type(second)) == (list, list):
        if len(first) == len(second) == 0:
            return 0
        if len(first) == 0:
            return 1
        elif len(second) == 0:
            return -1
        result = compareItems(first[0], second[0])
        if result == 0:
            return compareItems(first[1:], second[1:])
        return result


elements = []

for i in range(len(lines) // 2):
    first, second = lines[i * 2], lines[i * 2 + 1]
    if compareItems(ast.literal_eval(first), ast.literal_eval(second)) == 1:
        elements.append(i + 1)

print(sum(elements))
