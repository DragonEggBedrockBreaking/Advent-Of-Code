import functools
import re

with open("input.txt", "r", encoding="utf8") as f:
    first, second = f.read().split("\n\n")
    first, second = first.splitlines(), second.splitlines()

data = {}
for line in first:
    match = re.search(r'(.*){(.*)}', line)
    data[match.group(1)] = tuple(str(match.group(2)).split(","))
ranges = []


def traverse(current="in", x=(1, 4000), m=(1, 4000), a=(1, 4000), s=(1, 4000)):
    global ranges
    for condition in data[current]:
        if condition == "A":
            ranges.append((x, m, a, s))
        elif condition != "R":
            if ":" not in condition:
                traverse(condition, x, m, a, s)
            else:
                cond, dest = condition.split(":")
                if ">" in cond:
                    var, num = cond.split(">")
                    match var:
                        case "x":
                            if int(num) < x[0]:
                                if dest == "A":
                                    ranges.append((x, m, a, s))
                                elif dest != "R":
                                    traverse(dest, x, m, a, s)
                            elif int(num) < x[1]:
                                traverse(current, (int(num) + 1, x[1]), m, a, s)
                                traverse(current, (x[0], int(num)), m, a, s)
                        case "m":
                            if int(num) < m[0]:
                                if dest == "A":
                                    ranges.append((x, m, a, s))
                                elif dest != "R":
                                    traverse(dest, x, m, a, s)
                            elif int(num) < m[1]:
                                traverse(current, x, (int(num) + 1, m[1]), a, s)
                                traverse(current, x, (m[0], int(num)), a, s)
                        case "a":
                            if int(num) < a[0]:
                                if dest == "A":
                                    ranges.append((x, m, a, s))
                                elif dest != "R":
                                    traverse(dest, x, m, a, s)
                            elif int(num) < a[1]:
                                traverse(current, x, m, (int(num) + 1, a[1]), s)
                                traverse(current, x, m, (a[0], int(num)), s)
                        case "s":
                            if int(num) < s[0]:
                                if dest == "A":
                                    ranges.append((x, m, a, s))
                                elif dest != "R":
                                    traverse(dest, x, m, a, s)
                            elif int(num) < s[1]:
                                traverse(current, x, m, a, (int(num) + 1, s[1]))
                                traverse(current, x, m, a, (s[0], int(num)))
                elif "<" in cond:
                    var, num = cond.split("<")
                    match var:
                        case "x":
                            if int(num) > x[1]:
                                if dest == "A":
                                    ranges.append((x, m, a, s))
                                elif dest != "R":
                                    traverse(dest, x, m, a, s)
                            elif int(num) > x[0]:
                                traverse(current, (x[0], int(num) - 1), m, a, s)
                                traverse(current, (int(num), x[1]), m, a, s)
                        case "m":
                            if int(num) > m[1]:
                                if dest == "A":
                                    ranges.append((x, m, a, s))
                                elif dest != "R":
                                    traverse(dest, x, m, a, s)
                            elif int(num) > m[0]:
                                traverse(current, x, (m[0], int(num) - 1), a, s)
                                traverse(current, x, (int(num), m[1]), a, s)
                        case "a":
                            if int(num) > a[1]:
                                if dest == "A":
                                    ranges.append((x, m, a, s))
                                elif dest != "R":
                                    traverse(dest, x, m, a, s)
                            elif int(num) > a[0]:
                                traverse(current, x, m, (a[0], int(num) - 1), s)
                                traverse(current, x, m, (int(num), a[1]), s)
                        case "s":
                            if int(num) > s[1]:
                                if dest == "A":
                                    ranges.append((x, m, a, s))
                                elif dest != "R":
                                    traverse(dest, x, m, a, s)
                            elif int(num) > s[0]:
                                traverse(current, x, m, a, (s[0], int(num) - 1))
                                traverse(current, x, m, a, (int(num), s[1]))


traverse()
final = 0


def sum_arithmetic_series(start, end):
    num_terms = end - start + 1
    return num_terms * (start + end) // 2


def total_sum_of_combinations(rngs):
    sum_1 = sum_arithmetic_series(rngs[0][0], rngs[0][1])
    sum_2 = sum_arithmetic_series(rngs[1][0], rngs[1][1])
    sum_3 = sum_arithmetic_series(rngs[2][0], rngs[2][1])
    sum_4 = sum_arithmetic_series(rngs[3][0], rngs[3][1])

    total_sum = (
            sum_1 * (rngs[1][1] - rngs[1][0] + 1) * (rngs[2][1] - rngs[2][0] + 1) * (
            rngs[3][1] - rngs[3][0] + 1) +
            sum_2 * (rngs[0][1] - rngs[0][0] + 1) * (rngs[2][1] - rngs[2][0] + 1) * (
                    rngs[3][1] - rngs[3][0] + 1) +
            sum_3 * (rngs[0][1] - rngs[0][0] + 1) * (rngs[1][1] - rngs[1][0] + 1) * (
                    rngs[3][1] - rngs[3][0] + 1) +
            sum_4 * (rngs[0][1] - rngs[0][0] + 1) * (rngs[1][1] - rngs[1][0] + 1) * (
                    rngs[2][1] - rngs[2][0] + 1)
    )

    return total_sum


total = 0
for range in ranges:
    total += total_sum_of_combinations(range)
print(total)
