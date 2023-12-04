ifile = '2021/input/day10.txt'


points = {')': 3,']': 57,'}': 1197,'>': 25137}

data = open(ifile, "r").read().replace('\n','')

pars = {'(':')','{':'}','[':']','<':'>'}


to_close = []
err = 0
for i,p in enumerate(data):
    if p in pars: 
        to_close.append(pars[p])
    elif p == to_close[-1]:
        _ = to_close.pop()
    else:
        _ = to_close.pop()
        err += points[p]


def filter_corrupted(line):
    line = line.replace('\n','')
    to_close = []
    for i,p in enumerate(line):
        if p in pars: 
            to_close.append(pars[p])
        elif p == to_close[-1]:
            _ = to_close.pop()
        else:
            _ = to_close.pop()
            return False
    return True


with open(ifile) as f:
    out = list(filter(filter_corrupted,f.readlines()))



scoring = {')':1,']':2,'}':3,'>':4}

def complete_line(line):
    line = line.replace('\n','')
    to_close = []
    for i,p in enumerate(line):
        if p in pars: 
            to_close.append(pars[p])
        elif p == to_close[-1]:
            _ = to_close.pop()
        else:
            _ = to_close.pop()
    CloseSum=0
    while to_close:
        p = to_close.pop()
        CloseSum += CloseSum*5 + scoring[p]
    return CloseSum

part_two = sorted([complete_line(x) for x in out])
result_p2 = part_two[len(part_two)//2+1]


if __name__ == '__main__':
    print(f'result part one:')
    print(f'result of part two: {result_p2:.>20}')
