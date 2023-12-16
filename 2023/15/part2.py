with open("input.txt", "r", encoding="utf8") as f:
    line = f.read().splitlines()[0]


def hash(chars):
    s = 0
    for char in chars:
        s += ord(char)
        s *= 17
        s %= 256
    return s


boxes = {}
for part in line.split(","):
    label = part.split("-")[0].split("=")[0]
    box = hash(label)
    if box in boxes:
        if "-" in part:
            if any(x[0] == label for x in boxes[box]):
                boxes[box] = [x for x in boxes[box] if x[0] != label]
        else:
            flen = part.split("=")[1]
            if any(x[0] == label for x in boxes[box]):
                for i, v in enumerate(boxes[box]):
                    if v[0] == label:
                        boxes[box][i] = (label, flen)
            else:
                boxes[box].append((label, flen))
    else:
        if "=" in part:
            boxes[box] = [(label, part.split("=")[1])]

total = 0
for box, data in boxes.items():
    for i, item in enumerate(data):
        total += (int(box) + 1) * (i + 1) * int(item[1])

print(total)
