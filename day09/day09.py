from aocd import get_data
data = get_data(day=9).splitlines()
data = [int(x) for x in data]

def sumcheck(pre, num):
    a = 0
    pre.sort()
    while len(pre) > 0:
        b = len(pre)-1
        if pre[a] + pre[b] > num:
            pre.pop(b)
        elif pre[a] + pre[b] < num:
            pre.pop(a)
        else:
            return True
    return False 

sumset = [data.pop(0) for _ in range(25)]
while len(data) > 0:
    checknum = data[0]
    if sumcheck(sumset.copy(), checknum) == True:
        sumset.pop(0)
        sumset.append(data.pop(0))
    else:
        print(f"Invalid number: {checknum}")
        break
