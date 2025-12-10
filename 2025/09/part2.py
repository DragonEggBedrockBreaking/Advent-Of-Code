import itertools
import shapely.geometry as sg

with open("input.txt", "r", encoding="utf8") as f:
    coords = tuple(tuple(map(int, line.split(","))) for line in f.read().splitlines())

rectangle = lambda coord: (abs(coord[0][0]-coord[1][0])+1) * (abs(coord[0][1]-coord[1][1])+1)
polygon = sg.Polygon(coords)
print(max((abs(a-c)+1) * (abs(b-d)+1) for (a, b), (c, d) in sorted(itertools.combinations(coords, 2), key=rectangle, reverse=True) if polygon.contains(sg.box(a, b, c, d))))
