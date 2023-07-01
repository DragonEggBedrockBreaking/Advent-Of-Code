from statistics import mode
with open('data.txt', 'r') as f:
    data = f.read().splitlines()
strings = [[] for i in enumerate(data[0])]
for line in data:
    for i, bit in enumerate(line):
        strings[i].append(bit)
most_significant = [mode(bits) for bits in strings]
total = ''.join(most_significant)
total1 = ""
for char in total:
    match char:
        case "0": total1 += "1"
        case "1": total1 += "0"
print(int(total, 2) * int(total1, 2))
