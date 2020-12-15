from aocd import get_data
from sys import maxsize
import math
data = get_data(day=13).splitlines()
#data = ["939",
#"7,13,x,x,59,x,31,19"]
tr = int(data[0])
busses = data[1].split(",")
busclean = [int(x) if x!="x" else 0 for x in busses]
print(busclean)
inservice = [int(x) for x in busses if x != "x"]
check, ref = 99999, 0
for bus in inservice:
    if (bus - tr % bus) < check:
        check = (bus - tr % bus)
        ref = bus
print(f"Part 1: {check * ref}")
xl = 939490236001473 - 100
xxl = 939490236001473
#Part 2
vfl = False

for i in range(xl, xxl+1):
    for ind, bus in enumerate(busclean):
        valat = i+ind
        print (i, ind, bus, valat)
        if bus == 0:
            continue
        if i%bus != 0:
            vfl = False
            break
        if valat%bus != 0:
            print(valat%bus, "bad")
            vfl = False
            break
        else:
            print(valat%bus, "good")
            vfl = True
            continue
    if vfl == True:
        print(i)
        break

#with ChineseRemainderTheorem
i=0
M=1
e=0
for x in busclean:
    if x!=0: M*=x
j=0
while j<len(busclean):
    while busclean[j]==0: j+=1
    e+=-j*(M//busclean[j])*pow(M//busclean[j],-1,busclean[j])
    j+=1
print('part2',e%M)
