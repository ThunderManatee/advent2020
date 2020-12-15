from copy import deepcopy
from aocd import get_data
data = get_data(day=11).splitlines()
data = [[char for char in line] for line in data]
lenC, lenR = len(data)-1, len(data[0])-1

def get_sight_map(boat, adj):
    boatDict = {}
    for indR, row in enumerate(boat):
        for indS in range(len(row)):
            if boat[indR][indS] != ".":
                boatDict[(indR, indS)] = []
                searchMap = [(-1, -1), (-1, 0), (-1, 1),
                            (0,-1), (0, 1),
                            (1, -1), (1, 0), (1, 1)]
                searchMap = [(x,y) for x,y in searchMap if 0 <= indR+x <= lenC and 0 <= indS+y <= lenR]
                for i,j in searchMap:
                    x, y = indR+i, indS+j
                    while 0 <= x <= lenC and 0 <= y <= lenR:
                        if data[x][y] not in ("#", "L"):
                            if adj == True:
                                break
                            x, y = x+i, y+j
                        else:
                            boatDict[(indR, indS)].append((x,y))
                            break
    return boatDict

def seat_checker(map, data, oCheck):
    baseChart, deltaChart = [], deepcopy(data)
    while baseChart != deltaChart:
        occCount = 0
        baseChart = deepcopy(deltaChart)
        for (x, y), checks in map.items():
            seat = baseChart[x][y]
            dirtyDegens = 0
            for i,j in checks:
                if baseChart[i][j] == "#":
                    dirtyDegens += 1
            if seat == "L" and dirtyDegens == 0:
                deltaChart[x][y] = "#"
                occCount += 1
            elif seat == "#" and dirtyDegens >= oCheck:
                deltaChart[x][y] = "L"
            elif seat == "#" and dirtyDegens < oCheck:
                occCount += 1
    return occCount

print(f"Predicted Occupied Seats: {seat_checker(get_sight_map(data, True), data, 4)}")
print(f"Actual Occupied Seats: {seat_checker(get_sight_map(data, False), data, 5)}")
