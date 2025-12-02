with open("input.txt", "r", encoding="utf8") as f:
    data = f.read().splitlines()[0].split(",")

def is_invalid(identifier):
    half = len(identifier)//2
    return identifier[:half] == identifier[half:]

total = 0
for id_range in data:
    start, end = map(int, id_range.split("-"))
    for i in range(start, end + 1):
        if is_invalid(str(i)):
            total += i

print(total)