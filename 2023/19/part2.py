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
            break
        elif condition != "R":
            if ":" not in condition:
                traverse(condition, x, m, a, s)
                break
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
                                break
                            elif int(num) < x[1]:
                                traverse(current, (int(num) + 1, x[1]), m, a, s)
                                traverse(current, (x[0], int(num)), m, a, s)
                                break
                        case "m":
                            if int(num) < m[0]:
                                if dest == "A":
                                    ranges.append((x, m, a, s))
                                elif dest != "R":
                                    traverse(dest, x, m, a, s)
                                break
                            elif int(num) < m[1]:
                                traverse(current, x, (int(num) + 1, m[1]), a, s)
                                traverse(current, x, (m[0], int(num)), a, s)
                                break
                        case "a":
                            if int(num) < a[0]:
                                if dest == "A":
                                    ranges.append((x, m, a, s))
                                elif dest != "R":
                                    traverse(dest, x, m, a, s)
                                break
                            elif int(num) < a[1]:
                                traverse(current, x, m, (int(num) + 1, a[1]), s)
                                traverse(current, x, m, (a[0], int(num)), s)
                                break
                        case "s":
                            if int(num) < s[0]:
                                if dest == "A":
                                    ranges.append((x, m, a, s))
                                elif dest != "R":
                                    traverse(dest, x, m, a, s)
                                break
                            elif int(num) < s[1]:
                                traverse(current, x, m, a, (int(num) + 1, s[1]))
                                traverse(current, x, m, a, (s[0], int(num)))
                                break
                elif "<" in cond:
                    var, num = cond.split("<")
                    match var:
                        case "x":
                            if int(num) > x[1]:
                                if dest == "A":
                                    ranges.append((x, m, a, s))
                                elif dest != "R":
                                    traverse(dest, x, m, a, s)
                                break
                            elif int(num) > x[0]:
                                traverse(current, (x[0], int(num) - 1), m, a, s)
                                traverse(current, (int(num), x[1]), m, a, s)
                                break
                        case "m":
                            if int(num) > m[1]:
                                if dest == "A":
                                    ranges.append((x, m, a, s))
                                elif dest != "R":
                                    traverse(dest, x, m, a, s)
                                break
                            elif int(num) > m[0]:
                                traverse(current, x, (m[0], int(num) - 1), a, s)
                                traverse(current, x, (int(num), m[1]), a, s)
                                break
                        case "a":
                            if int(num) > a[1]:
                                if dest == "A":
                                    ranges.append((x, m, a, s))
                                elif dest != "R":
                                    traverse(dest, x, m, a, s)
                                break
                            elif int(num) > a[0]:
                                traverse(current, x, m, (a[0], int(num) - 1), s)
                                traverse(current, x, m, (int(num), a[1]), s)
                                break
                        case "s":
                            if int(num) > s[1]:
                                if dest == "A":
                                    ranges.append((x, m, a, s))
                                elif dest != "R":
                                    traverse(dest, x, m, a, s)
                                break
                            elif int(num) > s[0]:
                                traverse(current, x, m, a, (s[0], int(num) - 1))
                                traverse(current, x, m, a, (int(num), s[1]))
                                break


total = 0
traverse()
for rng in set(ranges):
    total += (rng[0][1] - rng[0][0] + 1) * (rng[1][1] - rng[1][0] + 1) * (rng[2][1] - rng[2][0] + 1) * (rng[3][1] - rng[3][0] + 1)
print(total)
