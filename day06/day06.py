from aocd import get_data
data = get_data(day=6).split("\n\n")
p1, p2 = 0, 0
alpha = "abcdefghijklmnopqrstuvwxyz"
for line in data:
    ansList = list(line.replace("\n", ""))
    p1 += len(set(ansList))
    groupSize = line.count("\n")+1
    for letter in alpha:
        if ansList.count(letter) == groupSize:
            p2 += 1
print(p1)
print(p2)