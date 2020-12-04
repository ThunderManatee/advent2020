from aocd import get_data
import copy
import re
data = get_data(day=4).split("\n\n")
presence = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
isValid = False
part1, part2 = 0, 0

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
    min, max = (150, 193) if mes == "cm" else (59, 76)
    return min <= int(num) <= max
def hcl(value): 
    return re.search(r"\A[#]\w{6}\Z", value)
def ecl(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
def pid(value): 
    return re.search(r"\A\d{9}\Z", value)

processor = {"byr": byr, "iyr": iyr, "eyr": eyr, "hgt": hgt, "hcl": hcl, "ecl": ecl, "pid": pid}

for line in data:
    line = {x.split(":")[0]: x.split(":")[1] for x in line.split()}
    f = [i for i in line.keys() if i in presence]
    if len(f) == len(presence):
        part1 += 1
        for field in presence:
            func = processor.get(field)
            isValid = func(line[field])
            if not isValid:
                break
        if isValid: part2 += 1
print(f"The number of passports with all required fields is {part1}.")
print(f"The number of passports with all required fields and valid values is {part2}.") 
