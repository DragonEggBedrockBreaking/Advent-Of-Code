import math
with open("input.txt", "r", encoding="utf8") as f:
    sections = f.read().split("\n\n")
regions = [(math.prod(map(int, section.split(": ")[0].split("x"))),
            tuple(enumerate(map(int, section.split(": ")[1].split()))))
           for section in sections.pop().splitlines()]
shapes = {int(section.split(":\n")[0]): section.split(":\n")[1].count("#") for section in sections}
print(sum(map(lambda region: region[0] >= sum(map(lambda data: shapes[data[0]] * data[1], region[1])), regions)))
