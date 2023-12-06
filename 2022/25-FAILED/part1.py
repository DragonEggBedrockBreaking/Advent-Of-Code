from math import log

with open("data.txt", "r") as f:
    lines = f.read().splitlines()

nums = {"-": -1, "=": -2}
reverse = {-1: "-", -2: "="}

total = 0
for line in lines:
    num = 0
    for i, char in enumerate(reversed(line)):
        if char in nums.keys():
            num += 5 ** i * nums[char]
        else:
            num += 5 ** i * int(char)
    total += num

dec = ""
for _ in range(int(log(total, 5)) + 1):
    total, modulus = divmod(total, 5)
    if modulus == 3:
        total += 1
        modulus = -2
    elif modulus == 4:
        total += 1
        modulus = -1
    dec += str(modulus) if modulus not in reverse.keys() else reverse[modulus]

print(dec[::-1])