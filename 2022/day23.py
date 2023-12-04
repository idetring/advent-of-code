ifile = '2022/input/day23.txt'
tfile = '2022/input/day23test.txt'

from collections import Counter
from dataclasses import dataclass
import numpy as np


DIRS = {'N':[1,0],'S':[-1,0],'W':[0,-1],'E':[0,-1],
        'NE':[1,1], 'NW':[1,-1], 'SE':[-1,1], 'SW':[-1,-1]
}

ORDER = {'N':[DIRS['NW'],DIRS['N'],DIRS['NE']],
        'S':[DIRS['SW'],DIRS['S'],DIRS['SE']],
        'W':[DIRS['NW'],DIRS['W'],DIRS['SW']],
        'E':[DIRS['NE'],DIRS['E'],DIRS['SE']]}


def listsum(x,y):
    return [xx+yy for xx,yy in zip(x,y)]

def put_back(X):
    return X[1:] + [X[0]]

@dataclass
class Elf:
    position : [int,int]
    new : []
    neighbours : []
    move : bool
    order = ['N','S','W','E']




data = open(tfile,mode='r').read().splitlines()
df = np.array([list(map(lambda x:x, [c for c in line])) for line in data])

elves = []
for r in range(len(df)):
    for c in range(len(df[0])):
        if df[r,c] == '#':
            elves.append(Elf((r,c),[],[],False))

positions = map(lambda x: x.position,elves)

print(f"{data}")