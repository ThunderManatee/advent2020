import re
from operator import xor
from aocd import get_data

data = [d for d in get_data(day=2).splitlines()]

def isValid(input: str):
    min, max, char, pwd = re.split('-|:\\s|\\s', input)
    min, max = int(min), int(max)

    return [min <= pwd.count(char) <= max, xor(pwd[min-1] == char, pwd[max-1] == char)]


c1, c2 = 0, 0
for d in data:
    res = isValid(d)
    c1 += res[0]
    c2 += res[1]
print(c1, c2)