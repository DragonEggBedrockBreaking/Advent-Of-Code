with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
total = 0
convert = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}


def getfirst(chars):
    for j, cha in enumerate(chars):
        if cha.isnumeric():
            return cha
        for k in range(1, 10):
            string = convert[k]
            if "".join(chars[j:min(j+len(string), len(chars)-1)]) == string:
                return str(k)
    return False


def getsecond(chars):
    for j, cha in enumerate(chars):
        if cha.isnumeric():
            return cha
        for k in range(1, 10):
            string = convert[k][::-1]
            if "".join(chars[j:min(j+len(string), len(chars)-1)]) == string:
                return str(k)
    return False


for line in lines:
    num = ""
    num += getfirst(line)
    num += getsecond(line[::-1])
    total += int(num)
print(total)
