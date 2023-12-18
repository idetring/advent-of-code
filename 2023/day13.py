import numpy as np

ifile = '2023/input/day13.txt'

def check_symmetry(p,smudge=0):
    for i in range(len(p)):
        if sum(c != d for l,m in zip(p[i-1::-1], p[i:])
                    for c,d in zip(l, m)) == smudge: return i
    else: return 0

def main(ifile):
    part1 = 0
    part2 = 0
    with open(ifile) as f:
        for mirror in f.read().split('\n\n'):
            mirrorlist = mirror.split('\n')
            ###
            horizontal = check_symmetry(mirrorlist) 
            vertical = check_symmetry([*zip(*mirrorlist)])
            part1 += horizontal*100 + vertical
            ###            
            horizontal = check_symmetry(mirrorlist,smudge=1) 
            vertical = check_symmetry([*zip(*mirrorlist)],smudge=1)
            part2 += horizontal*100 + vertical

    return part1,part2


if __name__ == "__main__":
    result1,result2= main(ifile)
    print('Result Part1',result1)
    print('Result Part2',result2)
