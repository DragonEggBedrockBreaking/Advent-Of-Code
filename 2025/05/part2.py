with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

ranges = [tuple(map(int, x.split("-"))) for x in lines if "-" in x]

while True:
    ranges.sort(key=lambda x: x[1], reverse=True)
    ranges.sort(key=lambda x: x[0])
    modifications = 0
    for i, (start, end) in enumerate(ranges[:-1]):
        next_start, next_end = ranges[i+1]
        if end >= next_start:
            ranges[i] = (start, max(end, next_end))
            del ranges[i+1]
            modifications += 1
            break
    else:
        break

print(sum((y-x+1) for x, y in ranges))


