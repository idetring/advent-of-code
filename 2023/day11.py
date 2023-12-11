import re

def counting():
    count=0
    def key():
        nonlocal count
        count+=1
        return count
    return key

Counter = counting()

class Galaxy:
    def __init__(self,position):
        self.id = Counter()
        self.position = position

    def __str__(self):
        return f"""{self.id}@{self.position}"""

def main(ifile):
    Galaxies = []
    data  = open("2023/input/day11.txt", "r", encoding="utf-8").read().splitlines()
    datatest = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".splitlines()
    df =     [[k for k in line] for line in data]

    emptyrows = [i for i,line in enumerate(df) if all([k == '.' for k in line])]
    emptycols = [i for i,col in enumerate(zip(*df)) if all([k == '.' for k in col])]

    Galaxies = []
    [[Galaxies.append(Galaxy([i,j])) for j,item in enumerate(row) if item == '#'] for i,row in enumerate(df)]

    def calc_distance(A,B,scale=1):    
        x = sorted([A.position[0],B.position[0]])
        y = sorted([A.position[1],B.position[1]])
        add_rows = sum([1 for er in emptyrows if x[0] < er < x[1]])
        add_cols = sum([1 for ec in emptycols if y[0] < ec < y[1]])
    
        if y[0] == y[1] and x[0] == x[1]:
            return 0
        if scale > 1:
            scale -= 1
        distance = (x[1] - x[0] + add_rows*(scale) ) + ( y[1]- y[0] + add_cols*(scale) )
        return distance

    a = [[calc_distance(i,j) for j in Galaxies] for i in Galaxies]

    result1 = sum([sum([a[i][j] for j in range(len(a)) if j < i]) for i in range(len(a))])
    b = [[calc_distance(i,j,scale=1000000) for j in Galaxies] for i in Galaxies]

    result2 = sum([sum([b[i][j] for j in range(len(b)) if j < i]) for i in range(len(b))])

    return result1,result2

if __name__ == '__main__':
    ifile = '2023/input/day11.txt'
    result1,result2 = main(ifile)
    print('Part 1:',result1)
    print('Part 2:',result2)