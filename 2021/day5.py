import numpy as np

with open("2021/input/day5.txt") as f:
    data = f.readlines()
data = [x.replace(' -> ', ',').split(',') for x in data]
data = [list(map(int, x)) for x in data]

size = max(max(x) for x in data) + 1
diagram = np.zeros((size, size), dtype=int)

for x1, y1, x2, y2 in data:
    x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    if x1 == x2 or y1 == y2:
        diagram[y1: y2+1, x1: x2+1] += 1

print(np.sum(diagram > 1))


size = max(max(x) for x in data) + 1
diagram = np.zeros((size, size), dtype=int)

for x1, y1, x2, y2 in data:
    if x1 == x2 or y1 == y2:
        x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        diagram[y1: y2+1, x1: x2+1] += 1
    else:
        x = range(x1, x2+1) if x1 <= x2 else range(x1, x2-1, -1)
        y = range(y1, y2+1) if y1 <= y2 else range(y1, y2-1, -1)
        for i, j in zip(x, y):
            diagram[j, i] += 1

print(np.sum(diagram > 1))