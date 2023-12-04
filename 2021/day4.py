from dataclasses import dataclass
import dataclasses


def define_group():
    """function to increase the counter for each line that only is a line break...."""
    counter=0
    def key(line):
        nonlocal counter
        if line == '\n':
            counter+=1
        return counter
    return key

@dataclass
class Card():
    B = []
    I = []
    N = []
    G = []
    O = []

GAME = 'BINGO'
GAMES={}
from itertools import groupby
with open("2021/input/day4.txt") as f:
    nums = f.readline().split(',')
    nums = [int(x) for x in nums]
    for key,group in groupby(f.readlines(),key=define_group()):
        GAMES[key]=Card() 
        i = 0
        for g in group:
            tmp = g.replace('\n','')
            if tmp != '':
                print(tmp)
                setattr(GAMES[key],GAME[i],[int(x) for x in tmp.split(' ') if x != ''])
                i+=1


def check_win(card):
    for letter in 'BINGO':
        if(len(set(getattr(card,letter)))==1):
            return True
    for i in range(5):
        cnt = 0
        for letter in 'BINGO':
            if getattr(card,letter)[i] == "X":
                cnt += 1
        if cnt == 5:
            return True
    return False



def mark_number(card,num):
    for letter in 'BINGO':
        for i in range(5):
            if getattr(card,letter)[i] == num:
                getattr(card,letter)[i] = 'X'


for n in nums:
    tmp = [mark_number(x,n) for x in GAMES.values()]
    won = [(x[0],check_win(x[1])) for x in GAMES.items()]
    if len(GAMES) > 1:
        for x in won:
            if x[1]:
                del GAMES[x[0]]
    if len(GAMES) == 1 and won[0][1]:
        break


def sum_of_card(card):
    cnt = 0
    for letter in 'BINGO':
        for i in range(5):
            if getattr(card,letter)[i] != "X":
                cnt += getattr(card,letter)[i]
    return cnt

sum_of_card(GAMES[42])*n
sum_of_card(GAMES[54])*n
