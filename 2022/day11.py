import operator
from itertools import groupby

ifile = '2022/input/day11.txt'
OPERS = {'*':operator.mul,"/":operator.truediv,'+':operator.add,'-':operator.sub}
TESTS = {'divisible':operator.mod}

def operation(oper,x):
    def key(old):
        return oper(old,x)
    return key

def test(oper,x):
    def key(old):
        if oper(old,x) == 0:
            return True
        return False
    return key

def define_monkey():
    """function to increase the counter for each line that only is a line break...."""
    counter=0
    def key(line):
        nonlocal counter
        if line == '\n':
            counter+=1
        return counter
    return key

class Monkey:
    def __init__(self,ID,items,operation,test,targets):
        self.ID = ID
        self.items = items
        self.operation = operation
        self.test = test
        self.targets = targets

    def __repr__(self):
        return f"""Monkey {self.ID}
  items: {self.items}
  targets: {self.targets}
  """

    N = 0

def parse_monkey(key,lines):
    monkey = {'ID':key,'target':[None,None]}
    for line in lines:
        IN = [i.strip() for i in line.split(':')]
        if IN != ['']:
            tmp = IN[1].strip().split(' ')
        if 'Starting items' in IN:
            monkey['items'] = [int(i) for i in IN[1].strip().split(',')]
        if 'Operation' in IN:
            if tmp[-1] == 'old':
                monkey['operation'] = operation(operator.pow,2)
            else:
                monkey['operation'] = operation(OPERS[tmp[-2]],int(tmp[-1]))
        if 'Test' in IN:
            monkey['test'] = test(TESTS[tmp[0]],int(tmp[-1]))
        if "If true" in IN:
            monkey['target'][1]=int(tmp[-1])
        if "If false" in IN:
            monkey['target'][0]=int(tmp[-1])
    m = Monkey(monkey['ID'],monkey['items'],monkey['operation'],monkey['test'],monkey['target'])
    return m

def part1_worry(item):
    return int(item/3)

def part2_worry(item):
    import numpy as np
    return np.sqrt(item)

def make_move(m,Ms,worry):
    # 
    item = m.items.pop(0)
    item = m.operation(item)
    item = worry(item)
    throw_to = m.targets[m.test(item)]
    Ms[throw_to].items.append(item)
    m.N += 1


def main(N,worry):

    # Parse input...
    Ms = []
    with open(ifile,mode='r') as f:
        for key,group in groupby(f,key=define_monkey()):
            Ms.append(parse_monkey(key,list(group)))


    # Make Round
    for n in range(N):
        if n % 100 == 0:
            print(n)
        for monk in Ms:
            while monk.items:
                make_move(monk,Ms,worry)
    # Make moves for each monkey....

    out = [m.N for m in Ms]
    out = sorted(out,reverse=True)
    return out[0]*out[1]



if __name__ == "__main__":
    print(f"part_one: {main(20,part1_worry)}")
    print(f"part_two: {main(10000,part2_worry)}")
    
