from aocd import get_data
from copy import deepcopy
data = get_data(day=8).split("\n")
data = [line.split() for line in data]
[line.append(0) for line in data]
swapList = []
cmdSwap = {"nop": "jmp", "jmp": "nop"}

def runner(instructions):
    addr,accm = 0,0
    while True:
        inlen = len(instructions)
        op,val,inc = instructions[addr]
        val = int(val)
        if addr == len(data)-1:
            return (f"boot success! code: {accm}")
        elif inc == 1:
            return f"infinite loop detected! code: {accm}"
        instructions[addr][2] += 1
        if op == "jmp":  
            addr += val
        elif op == "acc":
            accm += val
            addr += 1
        else:
            addr += 1

print(runner(deepcopy(data)))
print("fixing instruction set...")
for index in range(len(data)):
    if data[index][0] == "jmp" or data[index][0] == "nop":
        swapList.append((index,data[index]))

for ind, cmd in swapList:
    dalt = deepcopy(data)
    dalt[ind][0] = cmdSwap[cmd[0]]
    result = runner(dalt)
    if "success" in result:
        print(result)
        break
    
