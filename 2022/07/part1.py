with open("data.txt", "r") as f:
    lines = f.read().splitlines()

lines.append("$")
dirs = []
dirs_done = []
temp = []
dir_data = {}

for line in lines:
    if line.startswith("$"):
        if len(temp) > 0:
            dir_data[tuple(dirs)] = temp
            temp = []
        if "cd" in line:
            if ".." in line:
                dirs.pop()
            else:
                dirs.append(line.split()[-1])
    else:
        temp.append(line)


def get_size(dir):
    size = 0
    for item in dir_data[tuple(dir)]:
        if item.startswith("dir"):
            temp = list(dir)
            temp.append(item.split()[-1])
            size += get_size(temp)
        else:
            size += int(item.split()[0])
    return size


ans = 0

for key in dir_data:
    size = get_size(key)
    if size <= 100000:
        ans += size

print(ans)
