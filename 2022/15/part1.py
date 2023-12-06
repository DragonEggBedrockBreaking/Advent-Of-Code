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

LINE = 2000000

distances = []
for i, v in enumerate(sensors):
    distances.append(abs(v[0] - beacons[i][0]) + abs(v[1] - beacons[i][1]))

max_x_sensor = max(sensors, key=lambda x: x[0])[0]
max_x_beacon = max(beacons, key=lambda x: x[0])[0]
max_x = max_x_sensor if max_x_sensor > max_x_beacon else max_x_beacon

min_x_sensor = min(sensors, key=lambda x: x[0])[0]
min_x_beacon = min(beacons, key=lambda x: x[0])[0]
min_x = min_x_sensor if min_x_sensor < min_x_beacon else min_x_beacon

max_x += max(distances)
min_x -= max(distances)

count = 0
for i in range(min_x, max_x + 1):
    for j, v in enumerate(sensors):
        if (abs(v[0] - i) + abs(v[1] - LINE) <= distances[j]) and ((i, LINE) not in beacons):
            count += 1
            break

print(count)
