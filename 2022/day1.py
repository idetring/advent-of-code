# Day 1
ifile = '2022/input/day1.txt'
from itertools import groupby

def define_group():
    """function to increase the counter for each line that only is a line break...."""
    counter=0
    def key(line):
        nonlocal counter
        if line == '\n':
            counter+=1
        return counter
    return key

def part_onetwo():
    data = {}
    with open(ifile) as f:
        for key, group in  groupby(f, key=define_group()):
            elfsum = sum([int(g.replace('\n','') or 0) for g in group])
            data[key+1] = elfsum

    cumsum = {0:0}
    for i in range(4): # len(data)): no need to calc everything...
        cumsum[i+1] = cumsum[i] + data.pop(max(data,key=data.get))
    return cumsum

if __name__ == "__main__":
    res = part_onetwo()
    print(f'result part one: {res[1]:.>10}')
    print(f'result part two: {res[3]:.>10}')
