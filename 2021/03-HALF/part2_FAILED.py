from copy import deepcopy
with open('data.txt', 'r') as f:
    data = f.read().splitlines()
strings = []
def gen_strings_list(ls):
    global strings
    strings = [[] for i in enumerate(ls[0])]
    for line in ls:
        for i, bit in enumerate(line):
            strings[i].append(bit)
gen_strings_list(data)
number_of_ones = lambda index: sum(1 for bit in strings[index] if bit == "1")
number_of_zeros = lambda index: sum(1 for bit in strings[index] if bit == "0")
most_significant = lambda index: "1" if number_of_ones(index) >= number_of_zeros(index) else "0"
least_significant = lambda index: "1" if number_of_ones(index) <= number_of_zeros(index) else "0"
most_significant_values = [most_significant(i) for i in range(len(strings))]
least_significant_values = [least_significant(i) for i in range(len(strings))]
ogr, csr = deepcopy(data), deepcopy(data)
for i in range(len(most_significant_values)):
    for index in range(len(ogr), 0, -1):
        if len(ogr) <= 1:
            break
        if most_significant_values[i] != ogr[index - 1][i]:
            del ogr[index - 1]
            gen_strings_list(ogr)
    else:
        continue
    break
for i in range(len(least_significant_values)):
    for index in range(len(csr), 0, -1):
        if len(csr) <= 1:
            break
        if least_significant_values[i] != csr[index - 1][i]:
            del csr[index - 1]
            gen_strings_list(csr)
    else:
        continue
    break
print(most_significant_values, least_significant_values)
print(ogr, csr)
print(int(ogr[0], 2) * int(csr[0], 2))
