from functools import reduce  # forward compatibility for Python 3
import operator
from dataclasses import dataclass 
import re

ifile = '2022/input/day7.txt'

def switch():
    status = 0
    def key():
        nonlocal status
        if status:
            status = 0
        else:
            status = 1
        return status
    return key

directory = []
FileStructure={}

@dataclass
class File:
    name : str
    size : int

def go_back(directory):
    directory = directory[:-1]
    if directory:
        return directory
    return ['','/']

def go_root(directory):
    directory = ['','/']
    return directory

def get_directory(directory):
    return reduce(operator.getitem, directory, FileStructure)

def create_directory(directory):
    get_directory(directory[:-1])[directory[-1]] = {'FILES':[],'SIZE':0}

def add_file(directory,file):
    get_directory(directory)['FILES'].append(file)

def parse_ls(line):
    a,b = line.replace('\n','').split(' ')
    if a == 'dir':
        create_directory(directory+[b,])
    else:
        add_file(directory,File(b,int(a)))

directory=[]
FileStructure={'SIZE':0}
directory+=['']
create_directory(directory)
directory+=['/']
create_directory(directory)
with open(ifile,mode='r') as f:
## LOGIC:
## READLINE
## if starts with $ get command from dict CMD
## if ls read until next $ and get commands from CMD['ls']
    line = f.readline()
    for line in f.readlines():
        if line.startswith('$'):
            line = line.replace('\n','').replace('$ ','').split(' ')
            if line[0] == 'cd':
                if line[1] == '..':
                    directory = go_back(directory)
                elif line[1] == '/':
                    directory = go_root(directory)
                else:
                    directory += [line[1],]
        else:
            parse_ls(line)


def filesizes(filelist):
    size = 0
    for f in filelist:
        size+=f.size
    return size

def calc_size(d):
    for k, v in d.items():
        if isinstance(v, dict):
            d['SIZE'] += calc_size(v)
        elif k == 'FILES':
            d['SIZE'] += filesizes(v)      
    return d['SIZE']

def calc_sum(d):
    tmpsum = 0
    for k, v in d.items():
        if isinstance(v, dict):
            tmpsum += calc_sum(v)
        if isinstance(v,int):
            if v <= 100000:
                tmpsum += v 
    return tmpsum

calc_size(FileStructure)
totalsum = calc_sum(FileStructure)


# Part Two... Free some space:

N = 70000000
B = 30000000
V = 44125990

A = []
def calc_min(d):
    tmpmin = N
    for k, v in d.items():
        if isinstance(v, dict):
            print(f'{k:.^10}')
            tmpmin = min(tmpmin,calc_min(v))
        if isinstance(v,int):
            if v > V-B:
                print(f'{V-B:.<10}')
                print(f'{v:.>10}')
                tmpmin = min(tmpmin,v) 
    return tmpmin

A = []
def return_size(d):
    for k, v in d.items():
        if isinstance(v, dict):
            print(f'{k:.^10}')
            return_size(v)
        if isinstance(v,int) and k == 'SIZE':
                A.append(v) 


min(filter(lambda x: x > abs(N-V-B),A))