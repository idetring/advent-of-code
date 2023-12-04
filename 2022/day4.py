import numpy as np
import re

def parse_line(line):
    a, b, c, d = map(int, re.findall(r"\d+", line))
    return [a,b],[c,d]

def filter_func(line,func):
    X,Y = parse_line(line)
    Z = func(X,Y)
    if Z in [X,Y]:
        return True
    else: 
        return False

def filter_include(X,Y):
    ''' if min(x,y)'''
    return [min(X[0],Y[0]),max(X[1],Y[1])]

def filter_overlap(X,Y):
    return sorted([min(X[1],Y[0]),max(X[0],Y[1])])

def part_onetwo(func):
    out=''
    with open("2022/input/day4.txt", encoding='utf-8') as f:
        out = list(filter(lambda x:filter_func(x,func),f.readlines()))
    filtered = len(list(out))
    print(filtered)


if __name__ == '__main__':
    print(f'result part one:')
    part_onetwo(filter_include)
    print(f'result part two:')
    part_onetwo(filter_overlap)