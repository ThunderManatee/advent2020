data = [1, 12, 0, 20, 8, 16]
countd, lnum = {}, 0
countd = {x: i+1 for i, x in enumerate(data)}
lnum = data[-1]
ltrn = 30000000
for i in range(len(data), ltrn):
    if lnum not in countd.keys():
        countd[lnum] = i
    spk = i-countd[lnum]
    countd[lnum] = i
    lnum = spk
print(f"The {ltrn}th number is {lnum}.")
    
        
