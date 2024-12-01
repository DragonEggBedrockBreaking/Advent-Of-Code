list1, list2 = [], []

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f.read().splitlines():
        first, second = line.split("   ")
        list1.append(int(first))
        list2.append(int(second))

list1.sort()
list2.sort()
sum = 0
for i, v in enumerate(list1):
    sum += abs(v - list2[i])

print(sum)
