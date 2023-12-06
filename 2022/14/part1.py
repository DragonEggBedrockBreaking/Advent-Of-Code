with open("data.txt", "r") as f:
    lines = [[(int(y.split(",")[0]), int(y.split(",")[1]))
              for y in x.split(" -> ")] for x in f.read().splitlines()]

max_x = 0
min_x = 1000
max_y = 0

for line in lines:
    for x, y in line:
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y

min_x -= 1
max_x += 1
max_y += 1
grid = [["." for _ in range(min_x, max_x + 1)] for _ in range(max_y + 1)]
grid[0][500 - min_x] = "+"

for line in lines:
    for i in range(len(line) - 1):
        first_x, first_y = line[i]
        second_x, second_y = line[i + 1]
        if first_y < second_y:
            for j in range(first_y, second_y + 1):
                grid[j][first_x - min_x] = "#"
        elif second_y < first_y:
            for j in range(second_y, first_y + 1):
                grid[j][first_x - min_x] = "#"
        elif first_x < second_x:
            for j in range(first_x, second_x + 1):
                grid[first_y][j - min_x] = "#"
        elif second_x < first_x:
            for j in range(second_x, first_x + 1):
                grid[first_y][j - min_x] = "#"

sand_position = [500 - min_x, 0]

total = 0
while sand_position[1] < max_y:
    sand_position = [500 - min_x, 0]
    while True:
        x = sand_position[0]
        y = sand_position[1]
        if sand_position[1] >= max_y:
            break
        if grid[y + 1][x] == ".":
            sand_position[1] += 1
        elif grid[y + 1][x - 1] == ".":
            sand_position[1] += 1
            sand_position[0] -= 1
        elif grid[y + 1][x + 1] == ".":
            sand_position[1] += 1
            sand_position[0] += 1
        else:
            break
    grid[sand_position[1]][sand_position[0]] = "o"
    total += 1

print(total - 1)
