out = ""
steps=""

def get_stacks(out):
    out = out.split('\n')
    out = out[:-3]
    Nstacks = int(round(len(out[0])/4))

    Stacks = {}
    for i in range(1,Nstacks+1):
        Stacks[i] = ''
    for o in out:
        for i in range(1,len(o),4):
            if o[i] != ' ':
                Stacks[i//4+1] = Stacks[i//4+1]+o[i]
    return Stacks

def get_instructions(steps):
    steps = steps.split('\n')[:-1]
    return [read_line(x) for x in steps]

from dataclasses import dataclass
@dataclass
class Instruction:
    move : int
    fro : int 
    to : int

def read_line(line):
    a = int(line.split('move ')[1].split(' ')[0])
    b = int(line.split('from ')[1].split(' ')[0])
    c = int(line.split('to ')[1].split(' ')[0])
    return Instruction(a,b,c)

import re
out = ''
steps = ''

with open("2022/input/day5.txt") as f:
    # Read Starting Position....
    for line in f.readlines():
        if line.startswith('move'):
            steps+=line
        else: 
            out += line


Stacks = get_stacks(out)
Ins = get_instructions(steps)

def make_move(Stacks,IN):
    Stacks[IN.to] = Stacks[IN.fro][:IN.move][::-1] + Stacks[IN.to]
    Stacks[IN.fro] = Stacks[IN.fro][IN.move:]

def make_move_pack(Stacks,IN):
    Stacks[IN.to] = Stacks[IN.fro][:IN.move] + Stacks[IN.to]
    Stacks[IN.fro] = Stacks[IN.fro][IN.move:]


A = [make_move(Stacks,I) for I in Ins]
B = [make_move_pack(Stacks,I) for I in Ins]

ret = ''
for k,v in Stacks.items():
    ret += v[0]