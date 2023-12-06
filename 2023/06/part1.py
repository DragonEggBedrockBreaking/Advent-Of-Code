with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

times = [int(i) for i in lines[0].split()[1:]]
distances = [int(i) for i in lines[1].split()[1:]]
product = 1
for time, distance in zip(times, distances):
    count = 0
    for i in range(1, time + 1):
        if i * (time - i) > distance:
            count += 1
    product *= count

print(product)
