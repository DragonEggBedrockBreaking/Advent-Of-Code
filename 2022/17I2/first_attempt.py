# Gets data into string
with open("data2.txt", "r") as f:
    line = f.read().splitlines()[0]


def get_count(limit):
    # Defines line as a global variable
    global line

    # Generates a grid, with just a base length 7
    grid = [["-" for _ in range(7)]]

    # Some base variables - item keeps track of the shape, count keeps track
    # of how many shapes have dropped
    item = 0
    count = 0

    # Store a variable for potential limits
    potentials = []

    # Only drops 2022 shapes
    while count < limit:
        if count % 1000 == 0:
            print(count)
        # The starting co-ordinates of all of the points of each shape
        shapes = [
            [[[0, 2], [0, 3], [0, 4], [0, 5]], 1],
            [[[0, 3], [1, 2], [1, 3], [1, 4], [2, 3]], 3],
            [[[0, 4], [1, 4], [2, 2], [2, 3], [2, 4]], 3],
            [[[0, 2], [1, 2], [2, 2], [3, 2]], 4],
            [[[0, 2], [0, 3], [1, 2], [1, 3]], 2],
        ]

        # Every time all 5 items have been used, the index is reset
        if item == 5:
            item = 0

        # Gets the current shape
        shape = shapes[item]

        # Adds blanklines to the top of the grid - enough blanklines for the
        # height of the shape, plus 3 as a buffer between the falling shape and
        # the top one
        for i in range(3 + shape[1]):
            grid.insert(0, ["." for _ in range(7)])

        # Keeps iterating until broken out of
        while True:
            # Set the direction and edge index depending on the direction in input
            dy = -1 if line[0] == "<" else 1
            edge = 0 if line[0] == "<" else 6

            # Move the leftmost char in the string to the right end
            line = (line + line[0])[1:]

            # For each point in the shape, check if it is either on the edge (cannot
            # move further in that direction), or if there is something blocking its
            # movement
            for point in shape[0]:
                if (point[1] == edge) or (grid[point[0]][point[1] + dy] != "."):
                    break
            # If there is nothing blocking the movement, move each point one to the
            # appropriate direction
            else:
                for i in range(len(shape[0])):
                    shape[0][i][1] += dy

            # Do the same but with moving down - this time use a variable instead of
            # for-else so that we can run more code if the item is blocked
            can_drop = True
            for point in shape[0]:
                if grid[point[0] + 1][point[1]] != ".":
                    can_drop = False
                    break
            if can_drop:
                for i in range(len(shape[0])):
                    shape[0][i][0] += 1
            # If the item is blocked and cannot move further down, plot the item on
            # the grid and break out of the loop
            else:
                for point in shape[0]:
                    grid[point[0]][point[1]] = "#"
                break
        # Remove all empty lines from the top of the grid
        while "#" not in grid[0]:
            del grid[0]

        # Increment the counters
        item += 1
        count += 1

        if 1000000000000 % count == 0:
            ans = 1000000000000 / count * (len(grid) - 1)
            if str(ans).startswith("15142"):
                print((count, ans))
                potentials.append((count, ans))

    return potentials

# Print all the possible options, and then choose the correct one
for item in get_count(1000000):
    print(item)
