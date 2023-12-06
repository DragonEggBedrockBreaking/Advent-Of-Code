from z3 import Int, Solver, Abs

with open("data.txt", "r") as f:
    sensors = []
    beacons = []
    for x in f.read().splitlines():
        sensors.append(
            (int(x.split(":")[0].split("=")[-2].split(", ")[0]),
             int(x.split(":")[0].split("=")[-1])))
        beacons.append(
            (int(x.split(":")[1].split("=")[-2].split(", ")[0]),
             int(x.split(":")[1].split("=")[-1])))

MAX = 4000000

distances = []
for i, v in enumerate(sensors):
    distances.append(abs(v[0] - beacons[i][0]) + abs(v[1] - beacons[i][1]))

x = Int("x")
y = Int("y")
s = Solver()
s.add(x >= 0, x <= MAX, y >= 0, y <= MAX)

for i, v in enumerate(sensors):
    s.add(Abs(x - v[0]) + Abs(y - v[1]) > distances[i])

s.check()
m = s.model()
print(m[x].as_long() * 4000000 + m[y].as_long())
