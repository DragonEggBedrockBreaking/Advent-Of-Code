with (open("input.txt", "r", encoding="utf8") as f):
    line = "".join(f.read().splitlines())

dont = line.split("don't()")
for i, v in enumerate(dont):
    if i == 0:
        continue
    dont[i] = "".join(v.split("do()")[1:])
line = "".join(dont)

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
