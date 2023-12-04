import numpy as np

data = open("2021/input/day6.txt", encoding='utf-8').read()
df = np.array([int(x) for x in data.split(",")])

for day in range(80):
    df -= 1
    new = np.sum(df < 0)
    df = np.where(df < 0, 6, df)
    if new:
        df = np.hstack([df, np.full(new, 8)])
    print(f"After {day+1} days:", df)

print(df.shape)
# 362346


from collections import Counter

data = open("2021/input/day6.txt", encoding='utf-8').read()
df = Counter([int(x) for x in data.split(",")])
for i in range(-1, 9):
    if i not in df:
        df[i] = 0

for day in range(256):
    for i in range(9):
        df[i-1] = df[i]
    df[6] += df[-1]
    df[8] = df[-1]
    df[-1] = 0
    print(f"After {day+1} days:", df)

total = 0
for i in range(9):
    total += df[i]
print(total)