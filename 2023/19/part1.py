import re
with open("input.txt", "r", encoding="utf8") as f:
    first, second = f.read().split("\n\n")
    first, second = first.splitlines(), second.splitlines()

data = {}
for line in first:
    match = re.search(r'(.*){(.*)}', line)
    data[match.group(1)] = tuple(str(match.group(2)).split(","))

finals = []
for item in second:
    match = re.search(r'{x=(.*),m=(.*),a=(.*),s=(.*)}', item)
    variables = {"x": match.group(1), "m": match.group(2), "a": match.group(3), "s": match.group(4)}
    current = "in"
    final = ""
    while True:
        for condition in data[current]:
            if condition in "AR":
                final = condition
                break
            if ":" not in condition:
                current = condition
                break
            cond, dest = condition.split(":")
            if ">" in cond:
                var, num = cond.split(">")
                if int(variables[var]) > int(num):
                    if dest in "AR":
                        final = dest
                    else:
                        current = dest
                    break
            else:
                var, num = cond.split("<")
                if int(variables[var]) < int(num):
                    if dest in "AR":
                        final = dest
                    else:
                        current = dest
                    break
        if final:
            break
    finals.append(0 if final == "R" else sum(map(int, variables.values())))

print(sum(finals))
