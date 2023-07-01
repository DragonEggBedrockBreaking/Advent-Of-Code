index = 1
total = 0
top3 = [(0, 0), (0, 0), (0, 0)]

with open("data.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line == "":
            if total > top3[0][0]:
                top3[2] = top3[1]
                top3[1] = top3[0]
                top3[0] = (total, index)
            elif total > top3[1][0]:
                top3[2] = top3[1]
                top3[1] = (total, index)
            elif total > top3[2][0]:
                top3[2] = (total, index)
            if total > 69000:
                print(total, index)
            index += 1
            total = 0
        else:
            total += int(line)

print(top3[0][0] + top3[1][0] + top3[2][0])
print(top3)
