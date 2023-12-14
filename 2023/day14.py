import numpy as np
import itertools

ifile = '2023/input/day14.txt'

def parse_input(ifile):
    with open(ifile) as f:
        lines = [[l for l in line] for line in f.read().split('\n')]
        lines = np.array(lines)
    return lines

def tilt(lines):
    for c in range(lines.shape[1]):
        dy = 0
        for r in range(lines.shape[0]):
            char = lines[r,c]
            if char == '.':
                dy += 1
            elif char == '#':
                dy = 0
            else:
                lines[r,c] = '.'
                lines[r-dy,c] = 'O'

def round_tilt(lines):
    for i in range(4):
        tilt(lines)
        lines = np.rot90(lines,axes=(1,0))


def main(ifile):
    input = parse_input(ifile)
    tilt(input)
    part1 = sum([sum([1 for l in input[i] if l == 'O'])*(len(input)-i) for i in range( len(input)) ])

    input = parse_input(ifile)
    part2,states = [0],[0]
    while True:
        round_tilt(input)
        ##
        hashvalue = hash(input.tobytes())
        weightvalue = sum([sum([1 for l in input[i] if l == 'O'])*(len(input)-i) for i in range( len(input)) ])
        part2.append(weightvalue)
        if hashvalue in states:
            break
        states.append(hashvalue)
        ##
    cyclestart = states.index(hashvalue)
    cyclelength = len(states) - cyclestart
    cycleposition = (1_000_000_000 - cyclestart) % cyclelength + cyclestart
    part2 = part2[cycleposition]
    return part1,part2


if __name__ == "__main__":
    result1,result2= main(ifile)
    print('Result Part1',result1)
    print('Result Part2',result2)
