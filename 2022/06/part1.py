with open("data.txt", "r") as f:
    line = f.read().splitlines()[0]

final = 0

for i in range(len(line) - 3):
    if len(set(line[i:i+4])) == 4:
        final = i + 4
        break

print(final)
