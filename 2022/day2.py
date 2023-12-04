ifile = '2022/input/day2.txt'
## Chapter One
RPS = {}
# A: ROCK, B: PAPER, C: SCISSOR 
# X: ROCK, Y: PAPER, Z: SCISSOR
RPS['SCORE'] = {'X':1,'Y':2,'Z':3}
RPS['X'] = {'A':3,'B':0,'C':6}
RPS['Y'] = {'A':6,'B':3,'C':0}
RPS['Z'] = {'A':0,'B':6,'C':3}

score = 0
with open(ifile) as f:
    for line in f.readlines():
        line=line.replace('\n','')
        O,I = line.split(' ')
        score += RPS['SCORE'][I] + RPS[I][O]

## Chapter Two
# A: ROCK, B: PAPER, C: SCISSOR 
# X: LOSS, Y: DRAW, Z: WIN
RPS = {}
RPS['SCORE'] = {'A':1,'B':2,'C':3}
RPS['WLD'] = {'X':0,'Y':3,'Z':6}
RPS['X'] = {'A':'C','B':'A','C':'B'}
RPS['Y'] = {'A':'A','B':'B','C':'C'}
RPS['Z'] = {'A':'B','B':'C','C':'A'}

score = 0
with open(ifile) as f:
    for line in f.readlines():
        line=line.replace('\n','')
        O,I = line.split(' ')
        score += RPS['SCORE'][RPS[I][O]] + RPS['WLD'][I]

print(f'{score:.^10}')