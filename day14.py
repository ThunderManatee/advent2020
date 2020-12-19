from aocd import get_data
from itertools import product
data = get_data(day=14, year=2020).splitlines()

def generate_decs(breg, combl):
    declist = []
    for p in combl:
        treg = []
        p = list(p)
        for bit in breg:
            if bit == "X":
                treg.append(p.pop())
            else:
                treg.append(bit)
        treg = int("".join(str(x) for x in treg), 2)
        declist.append(treg)
    return declist

#Part 1
mask, mem = [], {}
for line in data:
    k, v = line.split(" = ")
    if k == "mask":
        mask = v
    else:
        reg = int(k[4:-1])
        v = int(v)
        lbin = [int(i) for i in bin(v)[2:]]
        v = [0 for _ in range(36-len(lbin))]
        v.extend(lbin)
        for i, m in enumerate(mask):
            if m != "X":
                v[i] = int(m)
        v = int("".join(str(x) for x in v), 2)
        mem[reg] = v
print(sum(mem.values()))

#Part 2
mask, mem = [], {}
for line in data:
    k, v = line.split(" = ")
    exes = 0
    if k == "mask":
        mask = v
    else:
        reg = int(k[4:-1])
        regbin = [i for i in f"{reg:036b}"]
        for i, m in enumerate(mask):
            if m != "0":
                regbin[i] = m
            if m == "X":
                exes += 1
        comb = [i for i in product(range(2), repeat = exes)]   
        for w in generate_decs(regbin, comb):
            mem[w] = int(v)
print(sum(mem.values()))
         


