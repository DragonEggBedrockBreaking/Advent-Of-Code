import re
import functools

with open("input.txt", "r", encoding="utf8") as f:
    first, second = f.read().split("\n\n")
    first, second = first.splitlines(), second.splitlines()

data = {}
for line in first:
    match = re.search(r'(.*){(.*)}', line)
    data[match.group(1)] = tuple(str(match.group(2)).split(","))

As = []
for i, value in enumerate(data.values()):
    for part in str(value).split(","):
        if "A" in part:
            As.append(i)

finals = set()


@functools.cache
def find_in(current, xrange=frozenset(range(1, 4001)), mrange=frozenset(range(1, 4001)),
            arange=frozenset(range(1, 4001)), srange=frozenset(range(1, 4001))):
    global finals
    if current == "in":
        finals = finals & [(x, m, a, s) for x in xrange for m in mrange for a in arange for s in srange]
        return
    for key, val in data.items():
        for pt in val:
            if current == pt:
                find_in(key, xrange, mrange, arange, srange)
            elif current in pt:
                newx, newm, newa, news = xrange, mrange, arange, srange
                if ">" in pt:
                    one, two = pt.split(":")[0].split(">")
                    match one:
                        case "x":
                            newx = frozenset(xrange | set(range(int(two) + 1, 4001)))
                        case "m":
                            newm = frozenset(mrange | set(range(int(two) + 1, 4001)))
                        case "a":
                            newa = frozenset(arange | set(range(int(two) + 1, 4001)))
                        case "s":
                            news = frozenset(srange | set(range(int(two) + 1, 4001)))
                elif "<" in pt:
                    one, two = pt.split(":")[0].split("<")
                    match one:
                        case "x":
                            newx = frozenset(xrange | set(range(1, int(two))))
                        case "m":
                            newm = frozenset(mrange | set(range(1, int(two))))
                        case "a":
                            newa = frozenset(arange | set(range(1, int(two))))
                        case "s":
                            news = frozenset(srange | set(range(1, int(two))))
                find_in(key, newx, newm, newa, news)


for i in As:
    print(i)
    find_in(list(data.keys())[i])
