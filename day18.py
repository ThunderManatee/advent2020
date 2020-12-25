from aocd import get_data
import re
data = get_data(day=18, year=2020).splitlines()
data = ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]


def math_blast(eq):
    eq = eq.replace(" ", "")
    eqn = ""
    while len(eq) > 0:
        cn, eq = eq[0], eq[1:]
        if cn == "(":
            er, eq = math_blast(eq)
            eqn += er
        elif cn.isalnum() or cn == "*" or cn == "+":
            eqn += cn
        elif cn == ")":
            return eqn, eq
        if re.fullmatch(r"\A\d+(\+|\*)\d+\Z", eqn):
            eqn = str(eval(eqn))
    return eqn, eq

def math_blaster(eq):
    eq = eq.replace(" ", "")
    print(eq)
    while not re.search(r"^\d+$", eq):
        while re.search(r"\([^\(\)]+\)", eq):
            inner = re.search(r"\([^\(\)]+\)", eq)
            ineq = inner.group(0)[1:-1]
            eq = eq.replace(inner.group(0), str(math_blaster(ineq)))
        while re.search(r"\d+\+\d+", eq):
            eqn = re.search(r"\d+\+\d+", eq)
            eres = eval(eqn.group(0))
            eq = eq.replace(eqn.group(0), str(eres))
        while re.search(r"\d+\*\d+", eq):
            eqn = re.search(r"\d+\*\d+", eq)
            eres = eval(eqn.group(0))
            eq = eq.replace(eqn.group(0), str(eres))
    return eq
    
print(sum([int(math_blast(eq)[0]) for eq in data]))

#Part 2
#for eq in data:
    #print(math_blaster(eq))
print(sum([int(math_blaster(eq)) for eq in data]))

