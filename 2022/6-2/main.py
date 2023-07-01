with open("data.txt", "r") as f:
    line = f.read().splitlines()[0]

final = 0

for i in range(len(line) - 13):
    if len(set(line[i:i+14])) == 14:
        final = i + 14
        break

print(final)
