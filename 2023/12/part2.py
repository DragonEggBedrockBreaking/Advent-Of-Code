import functools

with open("input.txt", "r", encoding="utf8") as f:
    lines = [("?".join([line.split()[0]] * 5), tuple(map(int, (line.split()[1].split(",") * 5)))) for line in f.read().splitlines()]


@functools.cache
def get_options(springs, info):
    if len(springs) == 0:
        return len(info) == 0
    if len(info) == 0:
        return "#" not in springs
    if len(springs) < info[0]:
        return 0
    options = 0
    if "." not in springs[:info[0]] and (len(springs) == info[0] or springs[info[0]] != "#"):
        options += get_options(springs[info[0] + 1:], info[1:])
    if springs[0] != "#":
        options += get_options(springs[1:], info)
    return options


total = 0
for data, counts in lines:
    total += get_options(data, counts)

print(total)
