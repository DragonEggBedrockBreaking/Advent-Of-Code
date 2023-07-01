with open("data.txt", "r") as f:
    equs = {equ.split(": ")[0]: equ.split(": ")[1] for equ in f.read().splitlines()}

def solve(equ):
    sec = equs[equ]
    if len(parts := sec.split()) > 1:
        match parts[1]:
            case "+":
                return solve(parts[0]) + solve(parts[2])
            case "-":
                return solve(parts[0]) - solve(parts[2])
            case "*":
                return solve(parts[0]) * solve(parts[2])
            case "/":
                return solve(parts[0]) // solve(parts[2])
    return int(sec)

print(solve("root"))
