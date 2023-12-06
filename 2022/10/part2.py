with open("data.txt", "r") as f:
    lines = f.read().splitlines()

pixels = []

x, p = 1, -1

for line in lines:
    p += 1

    if p == 40:
        p = 0
    if p in (x - 1, x, x + 1):
        pixels.append("#")
    else:
        pixels.append(".")

    if "addx" in line:
        p += 1

        if p == 40:
            p = 0
        if p in (x - 1, x, x + 1):
            pixels.append("#")
        else:
            pixels.append(".")

        x += int(line.split()[1])

print("".join(pixels[0:40]))
print("".join(pixels[40:80]))
print("".join(pixels[80:120]))
print("".join(pixels[120:160]))
print("".join(pixels[160:200]))
print("".join(pixels[200:240]))
