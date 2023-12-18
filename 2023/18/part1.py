from shapely import Polygon

with open("input.txt", "r", encoding="utf8") as f:
    lines = [tuple(line.split()[:2]) for line in f.read().splitlines()]
points = [(0, 0)]


def get_relative(direction, count):
    start = points[-1]
    match direction:
        case "U":
            return start[0] - count, start[1]
        case "D":
            return start[0] + count, start[1]
        case "L":
            return start[0], start[1] - count
        case "R":
            return start[0], start[1] + count
    return start


for d, c in lines:
    points.append(get_relative(d, int(c)))

pts = Polygon(points)
print(pts.area + sum([int(p[1]) for p in lines]) // 2 + 1)
