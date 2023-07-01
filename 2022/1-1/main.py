index = 1
total = 0
main = (0, 0)

with open("data.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line == "":
            if total > main[0]:
                main = (total, index)
            print(total, index)
            index += 1
            total = 0
        else:
            total += int(line)
            if index == 42:
                print(line)

print(main)
