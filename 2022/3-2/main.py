with open("data.txt", "r") as f:
    lines = f.read().splitlines()


def getascii(x):
    if x.islower():
        return ord(x) - 96
    return ord(x) - 64 + 26


score = 0

for i in range(len(lines) // 3):
    a, b, c = lines[i*3], lines[i*3+1], lines[i*3+2]
    repeated = ""
    mapa = {x: "" for x in a}
    mapb = {x: "" for x in b}
    for letter in c:
        if (letter in a) and (letter in b):
            repeated = letter
            break
    score += getascii(repeated)

print(score)
