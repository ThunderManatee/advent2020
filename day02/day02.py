import re
from operator import xor
from aocd import get_data

data = get_data(day=2)
dn = [d for d in data.splitlines()]

def isValid(input: str, p: int):
    min, max, char, pwd = re.split('-|:\\s|\\s', input)
    min, max = int(min), int(max)

    if p == 1:
        return min <= pwd.count(char) <= max
    return xor(pwd[min-1] == char, pwd[max-1] == char)


c1, c2 = 0, 0
for d in dn:
    c1 += isValid(d, 1)
    c2 += isValid(d, 2)
print(c1, c2)