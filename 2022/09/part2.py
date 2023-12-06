with open("data.txt", "r") as f:
    lines = f.read().splitlines()

positions = set()
positions.add((15, 11))
knots = [[15, 11] for _ in range(10)]

translations = {
    (-2, 0): (-1, 0),
    (2, 0): (1, 0),
    (0, 2): (0, 1),
    (0, -2): (0, -1),
    (-1, 2): (-1, 1),
    (-2, 1): (-1, 1),
    (-1, -2): (-1, -1),
    (-2, -1): (-1, -1),
    (1, 2): (1, 1),
    (2, 1): (1, 1),
    (1, -2): (1, -1),
    (2, -1): (1, -1),
    (-2, 2): (-1, 1),
    (-2, -2): (-1, -1),
    (2, 2): (1, 1),
    (2, -2): (1, -1)
}

for line in lines:
    for i in range(int(line.split()[1])):
        match line.split()[0]:
            case "U":
                knots[0][0] -= 1
            case "D":
                knots[0][0] += 1
            case "R":
                knots[0][1] += 1
            case "L":
                knots[0][1] -= 1

        for i in range(9):
            translation = (knots[i][0] - knots[i + 1][0], knots[i][1] - knots[i + 1][1])

            if translation in translations.keys():
                x, y = translations[translation]
                knots[i + 1][0] += x
                knots[i + 1][1] += y
        positions.add(tuple(knots[-1]))

print(len(positions))
