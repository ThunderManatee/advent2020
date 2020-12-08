import re
import string
from aocd import get_data
count1 = []

def sculpt(ugly):
    rules = {}
    for line in ugly:
        line = line.replace(" ", "")
        color, contents = line.split("bagscontain")
        contents = contents.split(",")
        rules[color] = []
        for item in contents:
            item = item.replace("bags", "").replace("bag", "").replace(".", "")
            if "noother" not in item:
                rules[color].append(re.split(r"(?<=[0-9])", item))
            else:
                rules[color].append(["0", item])
    return rules

def traverse(graph, color):
    for key, value in graph.items():
        for bag in value:
            if color in bag[1]:
                count1.append(key)
                traverse(graph, key)
    return count1

def inside(graph, color):
    count = 0
    for num, bag in graph[color]:
        if "noother" not in bag:
            count += int(num)
            count += int(num)*inside(graph, bag)
        else:
            return 0
    return count


data = get_data(day=7).split("\n")
print(len(set(traverse(sculpt(data), "shinygold"))))
print(inside(sculpt(data), "shinygold"))