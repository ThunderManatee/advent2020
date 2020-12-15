from aocd import get_data
from string import ascii_lowercase
data = get_data(day=6).split("\n\n")
p1, p2 = 0, 0
alpha = ascii_lowercase
for line in data:
    ansList = list(line.replace("\n", ""))
    p1 += len(set(ansList))
    groupSize = line.count("\n")+1
    for letter in alpha:
        if ansList.count(letter) == groupSize:
            p2 += 1
print(f"Any member answered: {p1}")
print(f"All members answered: {p2}")