from shapely import Polygon

with open("input.txt", "r", encoding="utf8") as f:
    lines = [(line.split()[0], line.split()[2]) for line in f.read().splitlines()]
points = [(0, 0)]


def get_relative(direction, count):
    start = points[-1]
    match direction:
        case "3":
            return start[0] - count, start[1]
        case "1":
            return start[0] + count, start[1]
        case "2":
            return start[0], start[1] - count
        case "0":
            return start[0], start[1] + count
    return start


for d, c in lines:
    points.append(get_relative(c[-2], int(c[2:-2], 16)))

pts = Polygon(points)
print(pts.area + sum([int(p[1][2:-2], 16) for p in lines]) // 2 + 1)
