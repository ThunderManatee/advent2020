from aocd import get_data
data = get_data(day=8).split("\n")
data = [line.split() for line in data]
[line.append(0) for line in data]
addr,accm = 0,0
while True:
    inlen = len(data)
    op,val,inc = data[addr]
    print (op,val,inc)
    if inc == 1:
        break
    data[addr][2] += 1
    if op == "jmp":
        if addr == inlen-2:
            addr+=1
        else:    
            addr += int(val)
    elif op == "acc":
        accm += int(val)
        addr += 1
    else:
        if data[addr+int(val)] == data[inlen-1]:
            addr += int(val)
        else:
            addr += 1
print(accm)

#TODO: Try running alternate instruction sets recursively
    
