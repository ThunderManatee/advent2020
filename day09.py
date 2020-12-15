from aocd import get_data
data = get_data(day=9).splitlines()
data = [int(x) for x in data]
#data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 
#95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
data1 = data.copy()

def sumCheck(pre, num):
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

checkNum = 0
sumset = [data1.pop(0) for _ in range(25)]
while len(data1) > 0:
    checkNum = data1.pop(0)
    if sumCheck(sumset.copy(), checkNum) == True:
        sumset.pop(0)
        sumset.append(checkNum)
    else:
        print(f"Invalid number: {checkNum}")
        data.pop(data.index(checkNum))
        break
ind = 0
dFlag = False
while dFlag == False:
    valArr = [data.pop(0)]
    for i in data:
        valArr.append(i)
        if sum(valArr) > checkNum:
            break
        if sum(valArr) == checkNum:
            valArr.sort()
            print(f"Encryption Weakness: {valArr[0] + valArr[-1]}")
            dFlag = True
            break
