import numpy as np
from itertools import product

ifile = '2021/input/day11.txt'
data = open(ifile, "r", encoding="utf-8").read()
df = np.array([list(map(int, [c for c in line])) for line in data.splitlines()])
r, c =  len(df), len(df[0])

count=0
n=0
while True:
    n+=1
    df += 1
    hasflashed = []
    flashed = [(m,n) for m,n in product(range(10),range(10)) if df[m][n] > 9]
    while flashed:
        hasflashed+=flashed # append all flashed points to list
        for i,j in flashed: 
            df[i,j] = 0 # set all flashed points to zero

        # all neighbours of flashed objects....
        temp = []
        for i,j in flashed:
            temp += [(m,n) for m,n in [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)] if m>=0 and m<r and n>=0 and n<c]

        # increase all of them except for those that have flashed in a previous step....
        for i,j in temp:
            df[i,j] +=1 if (i,j) not in hasflashed else 0

        flashed = [(m,n) for m,n in product(range(10),range(10)) if df[m][n] > 9]
    count+=len(hasflashed)
    if sum(sum(df == 0)) == 100:
        break