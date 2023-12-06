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

max_x_sensor = max(sensors, key=lambda x: x[0])[0]
max_y_sensor = max(sensors, key=lambda x: x[1])[1]
max_x_beacon = max(beacons, key=lambda x: x[0])[0]
max_y_beacon = max(beacons, key=lambda x: x[1])[1]
max_x = max_x_sensor if max_x_sensor > max_x_beacon else max_x_beacon
max_y = max_y_sensor if max_y_sensor > max_y_beacon else max_y_beacon

min_x_sensor = min(sensors, key=lambda x: x[0])[0]
min_y_sensor = min(sensors, key=lambda x: x[1])[1]
min_x_beacon = min(beacons, key=lambda x: x[0])[0]
min_y_beacon = min(beacons, key=lambda x: x[1])[1]
min_x = min_x_sensor if min_x_sensor < min_x_beacon else min_x_beacon
min_y = min_y_sensor if min_y_sensor < min_y_beacon else min_y_beacon

max_x += 5
max_y += 5
min_x -= 5
min_y -= 5

print(min_y, max_y)
grid = []
for i in range(min_y, max_y + 1):
    print(i)
    grid.append(["." for _ in range(min_x, max_x)])
#grid = [["." for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]
for i, v in enumerate(sensors):
    print(i)
    grid[v[1] - min_y][v[0] - min_x] = "S"
    grid[beacons[i][1] - min_y][beacons[i][0] - min_x] = "B"

for i, v in enumerate(sensors):
    print(i)
    distance = abs(v[0] - beacons[i][0]) + abs(v[1] - beacons[i][1]) + 1
    sx, sy = v[1] - min_x, v[0] - min_y
    expanse = distance
    while expanse >= 0:
        for j in range(sx - expanse + 1, sx + expanse):
            if (j < 0) or (j >= len(grid[0])) or (sy < 0) or (sy >= len(grid)):
                break
            if grid[sy][j] == ".":
                grid[sy][j] = "#"
        sy += 1
        expanse -= 1
    sx, sy = v[1] - min_x, v[0] - min_y
    expanse = distance
    while expanse >= 0:
        for j in range(sx - expanse + 1, sx + expanse):
            if (j < 0) or (j >= len(grid[0])) or (sy < 0) or (sy >= len(grid)):
                break
            if grid[sy][j] == ".":
                grid[sy][j] = "#"
        sy -= 1
        expanse -= 1

print(grid[10 - min_y].count("#"))
