import numpy as np

ifile = '2023/input/day10.txt'

dirs = {'upwards':np.array([[0,1,0],[0,0,0],[0,0,0]]),
        'downwards':np.array([[0,0,0],[0,0,0],[0,1,0]]),
        'leftwards':np.array([[0,0,0],[1,0,0],[0,0,0]]),
        'rightwards':np.array([[0,0,0],[0,0,1],[0,0,0]])}

symbols = {'|':np.array([[0,1,0],[0,0,0],[0,1,0]]),
        '-':np.array([[0,0,0],[1,0,1],[0,0,0]]),
        'L':np.array([[0,1,0],[0,0,1],[0,0,0]]),
        'J':np.array([[0,1,0],[1,0,0],[0,0,0]]),
        'F':np.array([[0,0,0],[0,0,1],[0,1,0]]),
        '7':np.array([[0,0,0],[1,0,0],[0,1,0]]),
        '.':np.array([[0,0,0],[0,0,0],[0,0,0]]),
        'S':np.array([[0,1,0],[1,0,1],[0,1,0]])}

connects = {'|':np.array([[0,1,0],[0,0,0],[0,1,0]]),
        '-':np.array([[0,0,0],[1,0,1],[0,0,0]]),
        'L':np.array([[0,0,0],[1,0,0],[0,1,0]]),
        'J':np.array([[0,0,0],[0,0,1],[0,1,0]]),
        'F':np.array([[0,1,0],[1,0,0],[0,0,0]]),
        '7':np.array([[0,1,0],[0,0,1],[0,0,0]]),
        '.':np.array([[0,0,0],[0,0,0],[0,0,0]]),
        'S':np.array([[0,1,0],[1,0,1],[0,1,0]])}
    
def connection(dir,Node,To):
    return dirs[dir] * symbols[Node.shape] * connects[To.shape]

class Node:
    def __init__(self,position,shape):
        self.position   = position
        self.shape = shape
        self.connections = []

    def __eq__(self,other):
        return self.position == other.position

    def __str__(self):
        out = f"""Node {self.position}\n   connections: {self.connections}\n"""
        return out

    def __repr__(self):
        out = f"""Node {self.position}\n   connections: {self.connections}\n"""
        return out

    def __contains__(self,item):
        return True if item == self.position else False
    
    def connecting(self,df):
        i,j = self.position
        r,c = len(df),len(df[0])
        if i > 0:
            if connection('upwards',self,df[i-1,j]).any():
                self.connections.append(df[i-1,j])
        if i+1 < r:
            if connection('downwards',self,df[i+1,j]).any():
                self.connections.append(df[i+1,j])
        if j > 0:
            if connection('leftwards',self,df[i,j-1]).any():
                self.connections.append(df[i,j-1])
        if j+1 < c:
            if connection('rightwards',self,df[i,j+1]).any():
                self.connections.append(df[i,j+1])


class Pfad:
    def __init__(self, previous,start,follow):
        self.previous = previous
        self.current = start
        self.next = follow
        self.count = 1
        self.start = start

    def __iter__(self):
        return self

    def __next__(self): 
        self.previous = self.current
        self.current = self.next
        self.next = [conn for conn in self.current.connections if conn != self.previous][0]
        self.count += 1
        if self.current != self.start:
            return self.current
        raise StopIteration



def main():
    data  = open("2023/input/day10.txt", "r", encoding="utf-8").read().splitlines()
    data2 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
""".splitlines()
    df = np.array([[Node(position=[i,j],shape=c) for j,c in enumerate(line)] for i,line in enumerate(data)])
    [[df[r,c].connecting(df) for c in range(df.shape[1])] for r in range(df.shape[0])]
    start = [[df[r,c] for c in range(df.shape[1]) if df[r,c].shape == 'S'] for r in range(df.shape[0]) ]
    start = [x for x in start if x != []]
    start = start[0][0]
    df[start.position] = Node(position=start.position,shape='|')
    genpfad = Pfad(start.connections[0],start,start.connections[1])
    nodes = [start,]
    for i in genpfad:
        newnode = i
        nodes.append(newnode)
    result1 = int(np.ceil((len(nodes))/2))

    is_region=False
    edge = None
    tiles = 0
    encapsulated = []
    for r in range(df.shape[0]):
        for c in range(df.shape[1]):
            if is_region and df[r,c] not in nodes:
                tiles +=1 
                encapsulated.append(df[r,c])

            elif df[r,c] in nodes:
                if df[r,c].shape == '|':
                    is_region = not is_region
                elif df[r,c].shape == '-':
                    continue

                if df[r,c].shape in "LF":
                    edge = df[r,c].shape
                # a pipe edge pointing to the left
                elif df[r,c].shape == "J":
                    # if previous edge wasn't pointing up
                    if edge == "F":
                        # switch region
                        is_region = not is_region
                    edge = None
                # a pipe edge pointing to the right
                elif df[r,c].shape == "7":
                    # if previous edge wasn't pointing down
                    if edge == "L":
                        # switch region
                        is_region = not is_region
                    edge = None

    return result1,len(encapsulated)+1

if __name__ == '__main__':
    result1,tiles = main()

    print('Part 1:',result1)
    print('Part 2:',tiles)