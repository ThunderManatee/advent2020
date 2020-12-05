from aocd import get_data
data = get_data(day=5).split("\n")
plane = [[x*8+y for x in range(128)] for y in range(8)]
rows = list(range(128))
cols = list(range(8))
    
def traverse(tKey, tList):
    if len(tList) > 1:
        mid = len(tList)//2
        if tKey[0] == "F" or tKey[0] == "L":
            return traverse(tKey[1:], tList[:mid])
        return traverse(tKey[1:], tList[mid:])    
    return tList[0]

gSeat = 0
emptyList = []
for line in data:
    rInput, cInput = line[:7],line[7:]
    assignedRow = traverse(rInput, rows)
    assignedCol = traverse(cInput, cols)
    plane[assignedCol][assignedRow] = -1
    seat = assignedRow*8 + assignedCol
    if seat > gSeat:
        gSeat =  seat
print(f"The highest occupied seat ID is {gSeat}.")
for cols in plane:
    for seat in cols:
        if seat != -1:
            emptyList.append(seat)
for seat in emptyList:
    if seat+1 not in emptyList and seat-1 not in emptyList:
        print(f"My seat ID is {seat}.") 