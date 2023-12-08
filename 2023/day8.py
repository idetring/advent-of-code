import re
import math

ifile = '2023/input/day8.txt'

def part1():
    return None

def part2():
    return None
    
def main():
    with open(ifile) as f:
        instructions = f.readline().strip()
        instructions = instructions.replace('R','1').replace('L','0')
        _ = f.readline()
        A = {}
        for line in f.readlines():
            a = re.findall('\w..',line)
            A[a[0]] = a[1:]
    i = 0
    a = 'AAA'
    while True:
        instr = int(instructions[i%len(instructions)])
        a = A[a][instr]
        i += 1
        if a == 'ZZZ':
            break
    result1 = i
    
    a = list(filter(lambda x:x.endswith('A'),A.keys()))
    result2 = []
    for aa in a:
        i = 0
        k = True
        while k:
            instr = int(instructions[i%len(instructions)])
            aa = A[aa][instr]
            i += 1
            if aa.endswith('Z'):
                result2.append(i)
                k = False
    result2 = math.lcm(*result2)
    return result1,result2

if __name__ == '__main__':
    result1,result2 = main()
    print('Result 1:',result1)
    print('Result 2:',result2)
