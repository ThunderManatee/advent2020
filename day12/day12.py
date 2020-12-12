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
    tmp = {"N": 0, "E": 0, "S": 0, "W": 0}
    if cmd in move.keys():
        wayp[cmd] += amt
        xdelta, ydelta = wayp["E"] - wayp["W"], wayp["N"] - wayp["S"]
        wdelta = {"N": ydelta, "E": xdelta, "S": -ydelta, "W": -xdelta}
        for d, a in wdelta.items():
            if a < 0 or a == 0:
                wayp[d] = 0
            else:
                wayp[d] = a
    elif cmd == "F":
        for card in movekeys:
            move[card] += amt*wayp[card]
    elif cmd == "R":
        s = amt/90
        for i in range(4):
            tmp[movekeys[int((i+s)%4)]] = wayp[movekeys[i]]
        wayp = tmp
    elif cmd == "L":
        s = amt/90
        for i in range(4):
            tmp[movekeys[int(i-s)]] = wayp[movekeys[i]]
        wayp = tmp
xpos = abs(move["N"] - move["S"])
ypos = abs(move["E"] - move["W"])
print(f"Distance from start by waypoint: {xpos+ypos}")

