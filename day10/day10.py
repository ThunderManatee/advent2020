from aocd import get_data
from collections import defaultdict
from typing import List
data = get_data(day=10).splitlines()
data = [int(x) for x in data]

def get_valid_nexts(value: int, adapters):
    return set(range(value + 1, value + 4)).intersection(adapters)

def build_clusters(input):
    # separate values into cluster by splitting on value-n - value-n+1 == 3
    input.sort()
    clusters = defaultdict(list)
    clusters[0].append(0)
    cluster_index = 0
    for index, val in enumerate(input, 1):
        clusters[cluster_index].append(val)
        if index == len(input):
            continue
        if input[index] - val == 3:
            cluster_index += 1

    return clusters

def build_chain(val, inputs, result):
        # recursively build valid chains
        if 1 <= len(inputs) <= 2:
            # short circuit trivial cases
            result["combos"] = 1
            return
        nexts = get_valid_nexts(val, inputs)

        for adapter in nexts:
            if max(inputs) == adapter:
                result["combos"] += 1
                continue
            build_chain(adapter, inputs, result)

data.sort()
print(data)
joltF, j1, j3 = 0, 0, 0
for j in data:
    if j - 1 == joltF:
        j1 += 1
    elif j - 3 == joltF:
        j3 += 1
    joltF = j
j3 += 1
data.sort()
clusters = build_clusters(data)
print(clusters)
results = {}
for index, cluster in clusters.items():
    results[index] = {"combos": 0}
    build_chain(min(cluster), cluster, results[index])
final = 1
for res in results.values():
    final *=res["combos"]
print(final)