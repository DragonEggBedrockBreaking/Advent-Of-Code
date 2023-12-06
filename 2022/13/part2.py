import ast
import functools

with open("data.txt", "r") as f:
    lines = f.read().splitlines()

while "" in lines:
    lines.remove("")

for i, v in enumerate(lines):
    lines[i] = ast.literal_eval(v)


def compareItems(first, second):
    if (type(first), type(second)) == (int, int):
        if first < second:
            return -1
        elif second < first:
            return 11
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
            return -1
        elif len(second) == 0:
            return 1
        result = compareItems(first[0], second[0])
        if result == 0:
            return compareItems(first[1:], second[1:])
        return result


lines.append([[2]])
lines.append([[6]])

lines = sorted(lines, key=functools.cmp_to_key(compareItems))
print((lines.index([[2]]) + 1) * (lines.index([[6]]) + 1))
