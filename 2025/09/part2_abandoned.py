import functools
import itertools

with open("input.txt", "r", encoding="utf8") as f:
    coords = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]
h_boundary = set()
v_boundary = set()
for p1, p2 in zip(coords, coords[1:] + [coords[0]]):
    (p1x, p1y), (p2x, p2y) = p1, p2
    if p1x == p2x:
        y0, y1 = min(p1y, p2y), max(p1y, p2y)
        h_boundary |= set((p1x, y) for y in range(y0, y1))
    else:
        x0, x1 = min(p1x, p2x), max(p1x, p2x)
        v_boundary |= set((x, p1y) for x in range(x0, x1))


@functools.cache
def in_polygon(coord):
    x, y = coord
    up = set((xi, y) for xi in range(x, -1, -1))
    left = set((x, yi) for yi in range(y, -1, -1))
    return (coord in (h_boundary | v_boundary)) or (bool(len(up & h_boundary) & 1) and bool(len(left & v_boundary) & 1))


def rectangle(coordinates):
    (a, b), (c, d) = coordinates
    x0, y0 = min(a, c), min(b, d)
    x1, y1 = max(a, c), max(b, d)
    pts = set((x0, yi) for yi in range(y0, y1+1))
    pts |= set((x1, yi) for yi in range(y0, y1+1))
    pts |= set((xi, y0) for xi in range(x0, x1+1))
    pts |= set((xi, y1) for xi in range(x0, x1+1))
    if all((in_polygon(c) for c in pts)):
        return abs(a-c+1) * abs(b-d+1)
    return 0


print(max(rectangle(cs) for cs in itertools.combinations(coords, 2)))
