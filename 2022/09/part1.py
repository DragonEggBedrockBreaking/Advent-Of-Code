with open("data.txt", "r") as f:
    lines = f.read().splitlines()

positions = set()
positions.add((4, 0))
head = [4, 0]
tail = [4, 0]

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
    (2, -1): (1, -1)
}

for line in lines:
    for i in range(int(line.split()[1])):
        match line.split()[0]:
            case "U":
                head[0] -= 1
            case "D":
                head[0] += 1
            case "R":
                head[1] += 1
            case "L":
                head[1] -= 1

        translation = (head[0] - tail[0], head[1] - tail[1])

        if translation in translations.keys():
            x, y = translations[translation]
            tail[0] += x
            tail[1] += y
        positions.add(tuple(tail))

print(len(positions))
