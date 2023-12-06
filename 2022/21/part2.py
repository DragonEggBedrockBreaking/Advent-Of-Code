from sympy import solve, Symbol, sympify

with open("data.txt", "r") as f:
    equs = {equ.split(": ")[0]: equ.split(": ")[1] for equ in f.read().splitlines()}


def solve_alg(equ):
    if equ == "humn":
        return equ
    sec = equs[equ]
    if len(parts := sec.split()) > 1:
        match parts[1]:
            case "+":
                return f"({solve_alg(parts[0])} + {solve_alg(parts[2])})"
            case "-":
                return f"({solve_alg(parts[0])} - {solve_alg(parts[2])})"
            case "*":
                return f"({solve_alg(parts[0])} * {solve_alg(parts[2])})"
            case "/":
                return f"({solve_alg(parts[0])} / {solve_alg(parts[2])})"
    return sec


def solve_math(equ):
    sec = equs[equ]
    if len(parts := sec.split()) > 1:
        match parts[1]:
            case "+":
                return solve_math(parts[0]) + solve_math(parts[2])
            case "-":
                return solve_math(parts[0]) - solve_math(parts[2])
            case "*":
                return solve_math(parts[0]) * solve_math(parts[2])
            case "/":
                return solve_math(parts[0]) // solve_math(parts[2])
    return int(sec)

parts = equs["root"].split(" + ")
humn = Symbol("humn")
print(solve(sympify(f"{solve_alg(parts[0])} - {solve_math(parts[1])}"), humn)[0])
