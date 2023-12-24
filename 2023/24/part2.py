from z3 import Int, Solver, sat

with open("input.txt", "r", encoding="utf8") as f:
    lines = []
    for x in f.read().splitlines():
        first, second = x.split(" @ ")
        lines.append((tuple(map(int, first.replace(" ", "").split(","))), tuple(map(int, second.replace(" ", "").split(",")))))

x = Int("x")
xv = Int("xv")
y = Int("y")
yv = Int("yv")
z = Int("z")
zv = Int("zv")
s = Solver()
i = 0
for (pos, vel) in lines:
    i += 1
    if i == 4:
        break
    t = Int("t" + str(i))
    s.add(pos[0] + vel[0] * t == x + xv * t)
    s.add(pos[1] + vel[1] * t == y + yv * t)
    s.add(pos[2] + vel[2] * t == z + zv * t)

if s.check() == sat:
    model = s.model()
    print(model[x].as_long() + model[y].as_long() + model[z].as_long())
