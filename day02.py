import re
from aocd import get_data

data = [d for d in get_data(day=2).splitlines()]

def isValid(input: str):
    min, max, char, pwd = re.split(r': |-|\s', input)
    min, max = int(min), int(max)

    return [min <= pwd.count(char) <= max, (pwd[min-1] == char) ^ (pwd[max-1] == char)]


c1, c2 = 0, 0
for d in data:
    count,pos = isValid(d)
    c1 += count
    c2 += pos
print(f"The number of valid passwords by count is {c1}.") 
print(f"The number of valid passwords by position is {c2}.")