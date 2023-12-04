def counting():
    counter=0
    def key():
        nonlocal counter
        counter+=1
        return counter
    return key

with open('2021/input/day1.txt') as f:
    DOWN,UP = counting(),counting()
    d,u = 0,0
    a = float(f.readline())
    for line in f.readlines():
        if a < float(line):
            d = DOWN()
        else:
            u = UP()
        a = float(line)


with open('2021/input/day1.txt') as f:
    DOWN,UP = counting(),counting()
    d,u = 0,0
    a = [float(f.readline()) for _ in range(3)]
    for line in f.readlines():
        b = a[1:]+[float(line)]
        if sum(a) < sum(b):
            d = DOWN()
        else:
            u = UP()
        a = b