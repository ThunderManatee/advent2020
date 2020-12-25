from aocd import get_data
data = get_data(day=22, year=2020)
# data = '''Player 1:
# 9
# 2
# 6
# 3
# 1

# Player 2:
# 5
# 8
# 4
# 7
# 10'''

player1, player2 = data.split("\n\n")
player1 = player1.splitlines()
player2 = player2.splitlines()
player1.remove("Player 1:")
player2.remove("Player 2:")

while len(player1) > 0 and len(player2) > 0:
    draw1 = int(player1.pop(0))
    draw2 = int(player2.pop(0))
    if draw1 > draw2:
        player1.append(draw1)
        player1.append(draw2)
    else:
        player2.append(draw2)
        player2.append(draw1)
score = 0
if len(player1) > 0:
    mul = len(player1)
    for i, c in enumerate(player1):
        score += abs(i-mul)*int(c)
if len(player2) > 0:
    mul=len(player2)
    for i, c in enumerate(player2):
        score += abs(i-mul)*int(c)
print(score)



