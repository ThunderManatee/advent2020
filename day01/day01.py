from aocd import get_data
data = get_data(day=1)
dn = [int(d) for d in data.split('\n')]

def part1(data):
    data.sort()
    a = 0
    b = len(data)-1
    while True:
        if data[a] + data[b] > 2020:
            b -= 1
        elif data[a] + data[b] < 2020:
            a += 1
        else:
            return data[a]*data[b]

def part2(data):
    data.sort()
    a = 0
    b = 1
    c = len(data)-1
    while True:
        if b > c:
            a += 1
            b = a+1
            c = len(data)-1
        sum = data[a] + data[b] + data[c]
        if sum > 2020:
            c -= 1
        elif sum < 2020:
            b += 1
        else:
            return data[a]*data[b]*data[c]


print(part1(dn))
print(part2(dn))
