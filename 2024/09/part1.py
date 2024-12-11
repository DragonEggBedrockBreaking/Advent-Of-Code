with open("input.txt", "r", encoding="utf8") as f:
    raw = list(int(v) for v in f.read().splitlines()[0])

structure = []
current = 0
for i, v in enumerate(raw):
    if i % 2:
        for _ in range(v):
            structure.append(".")
    else:
        for _ in range(v):
            structure.append(current)
        current += 1

while "." in structure:
    if structure[-1] == ".":
        structure.pop()
        continue
    end = structure.pop()
    structure[structure.index(".")] = end

total = 0
for i, item in enumerate(structure):
    total += i * item

print(total)
