# shoelace, pick theorem

import re
ifile = '2023/input/day18.txt'
directories = {'R':(1,0),'L':(-1,0),'U':(0,-1),'D':(0,1)}
directories2 = {'0':(1,0),'2':(-1,0),'3':(0,-1),'1':(0,1)}


def main(ifile):
    result1,result2 = 0,0

    with open(ifile) as f:
        data = list(map(str.split,f.readlines()))

    # Part1
    xpos = 0
    ypos = 1 
    for dir, step, color in data:
        step = int(step)
        x,y = directories[dir]
        xpos += x*step
        ypos += y*step * xpos + step/2

    result1 = int(ypos)

    # Part2 
    xpos = 0
    ypos = 1 
    for dir, step, color in data:
        step = int(color[2:-2],16)
        x,y = directories2[color[-2]]
        xpos += x*step
        ypos += y*step * xpos + step/2

    result2 = int(ypos)


    return result1,result2

if __name__ == '__main__':
    result1, result2 = main(ifile)
    print('Result Part1',result1)
    print('Result Part2',result2)

