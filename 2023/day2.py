import re

ifile = '2023/input/day2.txt'

"""12 red cubes, 13 green cubes, and 14 blue cubes"""

CubesDict = {'red':12,'blue':14,'green':13}

def CheckGame(X):
    b = X.split(':')
    GameID = int(b[0][5:])
    Rounds = b[1].split(';')
    for Round in Rounds:
        for Cubes in  Round.split(','):
            Draw = Cubes.strip().split()
            if CubesDict[Draw[1]] < int(Draw[0]):
                return 0

    return GameID

def CheckGame_Minimum(X):
    CubesDict = {'red':0,'blue':0,'green':0}
    b = X.split(':')
    GameID = int(b[0][5:])
    Rounds = b[1].split(';')
    for Round in Rounds:
        for Cubes in  Round.split(','):
            Draw = Cubes.strip().split()
            if CubesDict[Draw[1]] < int(Draw[0]):
                CubesDict[Draw[1]] = int(Draw[0])

    result = 1
    for _,value in CubesDict.items():
        result *= value

    return result


if __name__ == '__main__':
    Part1 = 0
    Part2 = 0
    with open(ifile) as f:
        for a in f.readlines():
            Part1 += CheckGame(a)
            Part2 += CheckGame_Minimum(a)

    print('Result Part 1:', Part1)
    print('Result Part 2:', Part2)
