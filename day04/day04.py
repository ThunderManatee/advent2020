from aocd import get_data
import copy
import re
data = get_data(day=4).split("\n\n")
data = [data[x].split() for x in range(len(data))]
presence = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] 
valid = 0

def byr(value): 
    return 1920 <= int(value) <= 2002
def iyr(value): 
    return 2010 <= int(value) <= 2020
def eyr(value): 
    return 2020 <= int(value) <= 2030
def hgt(value):
    if not re.search(r"\A\d{2,3}\D{2}\Z", value):
        return False
    num,mes = value[:-2], value[-2:]
    min = 150 if mes == "cm" else 59
    max = 193 if mes == "cm" else 76
    return min <= int(num) <= max
def hcl(value): 
    return re.search(r"\A[#]\w{6}\Z", value)
def ecl(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
def pid(value): 
    return re.search(r"\A\d{9}\Z", value)
def cid(value):
    return True

def processor(field) -> bool:
    op, val = field.split(":")
    print(op, val)
    switcher = {
        "byr": byr,
        "iyr": iyr,
        "eyr": eyr,
        "hgt": hgt,
        "hcl": hcl,
        "ecl": ecl,
        "pid": pid
    }
    if op == "cid": return True
    func = switcher.get(op)
    if func: 
        return func(val)
    else: 
        return False

for i in range(10):
    check = []
    for j in range(len(data[i])):
        if not processor(data[i][j]):
            break
        if data[i][j][:3] != "cid": 
            check.append(data[i][j][:3])
    if check.sort() == presence.sort():
        valid += 1
print(valid) 
