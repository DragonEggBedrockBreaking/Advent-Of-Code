with open("data.txt", "r") as f:
    lines = f.read().splitlines()


def getascii(x):
    if x.islower():
        return ord(x) - 96
    return ord(x) - 64 + 26


score = 0

for line in lines:
    repeated = ""
    map = {}
    for x in line[:len(line) // 2]:
        map[x] = ""
    for letter in line[len(line) // 2:]:
        if letter in map:
            repeated = letter
            break
    score += getascii(repeated)

print(score)
