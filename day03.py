from aocd import get_data
data = get_data(day=3).splitlines()

def toboggan(data, right, down):
    x, y, trees, rows, cols = 0, 0, 0, len(data), len(data[0])
    for y in range(0, rows, down):
        if data[y][x%cols] == "#":
            trees += 1
        x += right
    return trees

p2 = 1
slopes = ((1,1),(3,1),(5,1),(7,1),(1,2))
for right, down in slopes:
    aii = toboggan(data, right, down)
    if right == 3:
        print (f"Arboreal Impact Index for slope 3,1 is: {aii}.")
    p2 *= aii
print(f"Multiplicative Arboreal Impact Index: {p2}")