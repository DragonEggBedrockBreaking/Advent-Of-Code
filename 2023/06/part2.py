with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

time = int("".join(lines[0].split(":")[1].split()))
distance = int("".join(lines[1].split(":")[1].split()))
start, end = 0, 0
for i in range(1, time + 1):
    if i * (time - i) > distance:
        start = i
        break
for i in range(time, 0, -1):
    if i * (time - i) > distance:
        end = i
        break

print(end - start + 1)