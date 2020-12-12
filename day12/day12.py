from aocd import get_data
data = get_data(day=12).splitlines()
move, bear = {"N": 0, "E": 0, "S": 0, "W": 0}, 1
movekeys = list(move.keys())
xpos, ypos = 0, 0
for item in data:
    cmd, amt = item[0], int(item[1:])
    if cmd in move.keys():
        move[cmd] += amt
    elif cmd == "F":
        move[movekeys[bear]] += amt
    if cmd == "R":
        bear = int((bear+(amt/90))%4)
    elif cmd == "L":
        bear = int((bear-(amt/90)+4)%4)
xpos = abs(move["N"] - move["S"])
ypos = abs(move["E"] - move["W"])
print(f"Distance from start: {xpos+ypos}")

move = {"N": 0, "E": 0, "S": 0, "W": 0}
wayp = {"N": 1, "E": 10, "S": 0, "W": 0}
xpos, ypos = 0, 0
for item in data:
    cmd, amt = item[0], int(item[1:])
    if cmd in move.keys():
        wayp[cmd] += amt
        ydelta = wayp["N"] - wayp["S"]
        xdelta = wayp["E"] - wayp["W"]
        if ydelta > 0:
            wayp["N"], wayp["S"] = abs(ydelta), 0
        elif ydelta < 0:
            wayp["S"], wayp["N"] = abs(ydelta), 0
        else:
            wayp["N"], wayp["S"] = 0, 0
        
        if xdelta > 0:
            wayp["E"], wayp["W"] = abs(xdelta), 0
        elif xdelta < 0:
            wayp["W"], wayp["E"] = abs(xdelta), 0
        else:
            wayp["E"], wayp["W"] = 0, 0
    elif cmd == "F":
        for card in movekeys:
            move[card] += amt*wayp[card]
    elif cmd == "R":
        tmp = [0, 0, 0, 0]
        s = amt/90
        for i in range(4):
            tmp[int((i+s)%4)] = wayp[movekeys[i]]
        for i in range(4):
            wayp[movekeys[i]] = tmp[i]
    elif cmd == "L":
        tmp = [0, 0, 0, 0]
        s = amt/90
        for i in range(4):
            tmp[int(i-s)] = wayp[movekeys[i]]
        for i in range(4):
            wayp[movekeys[i]] = tmp[i]
xpos = abs(move["N"] - move["S"])
ypos = abs(move["E"] - move["W"])
print(f"Distance from start by waypoint: {xpos+ypos}")

