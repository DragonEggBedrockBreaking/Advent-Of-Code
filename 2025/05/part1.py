with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

fresh = 0
ranges = [tuple(map(int, x.split("-"))) for x in lines if "-" in x]
for item in map(int, lines[len(ranges)+1:]):
    for start, end in ranges:
        if start <= item <= end:
            fresh += 1
            break

print(fresh)
