from dataclasses import dataclass
@dataclass
class Position:
    X = 0.0
    Y = 0.0

def forward(submarine,x):
    submarine.X += x

def down(submarine,x):
    submarine.Y += x

def up(submarine,x):
    submarine.Y -= x

CMD = {'forward':forward,'down':down,'up':up}

submarine = Position()
with open('2021/input/day2.txt') as f:
    for line in f.readlines():
        cmd,x = line.split(' ')
        CMD[cmd](submarine,float(x))

submarine.X * submarine.Y


class Position:
    X = 0.0
    Y = 0.0
    depth = 0.0

def forward(submarine,x):
    submarine.X += x
    submarine.depth += submarine.Y * x

def down(submarine,x):
    submarine.Y += x

def up(submarine,x):
    submarine.Y -= x

CMD = {'forward':forward,'down':down,'up':up}

submarine = Position()
with open('2021/input/day2.txt') as f:
    for line in f.readlines():
        cmd,x = line.split(' ')
        CMD[cmd](submarine,float(x))

submarine.X * submarine.depth