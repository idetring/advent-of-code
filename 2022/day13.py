ifile = '2022/input/day13test.txt'


import ast
from itertools import groupby
def define_group():
    counter=0
    def key(line):
        nonlocal counter
        if line == '\n':
            counter+=1
        return counter
    return key

def switch():
    status = 'right'
    def key():
        nonlocal status
        if status == 'left':
            status = 'right'
        else:
            status = 'left'
        return status
    return key


df = {}
with open(ifile,mode='r') as f:
    for key,group in groupby(f,key=define_group()):
        tmp = {}
        a = switch()
        for line in group:
            if line != '\n':
                tmp[a()]=(ast.literal_eval(line))
        df[key]=tmp
        