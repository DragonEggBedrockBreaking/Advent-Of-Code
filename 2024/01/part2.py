list1, list2, set1 = [], [], set()

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f.read().splitlines():
        first, second = line.split("   ")
        list1.append(int(first))
        set1.add(int(first))
        list2.append(int(second))

sum = 0
for value in set1:
    sum += value * list1.count(value) * list2.count(value)

print(sum)
