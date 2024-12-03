with open("input.txt", "r", encoding="utf8") as f:
    line = "".join(f.read().splitlines())

total = 0
first_split = line.split("mul(")
for part in first_split:
    second_split = part.split(")")[0]
    third_split = second_split.split(",")
    if len(third_split) == 2:
        try:
            total += int(third_split[0]) * int(third_split[1])
        except ValueError:
            pass

print(total)
