import re

with open("input.txt", "r", encoding="utf8") as f:
    data = f.read().splitlines()[0].split(",")

total = 0
for id_range in data:
    start, end = map(int, id_range.split("-"))
    for i in range(start, end + 1):
        if re.match(r"^(\d+)\1+$", str(i)):
            total += i

print(total)