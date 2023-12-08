import itertools
import re

ifile = '2023/input/day7.txt'

Eval = [[1,1,1,1,1],[1,1,1,2],[1,2,2],[1,1,3],[2,3],[1,4],[5]]
cards = ['23456789TJQKA','J23456789TQKA']

def parse_line(line,func):
    hand,bid = line.split(' ')
    return (func(hand),int(bid))
    
def evaluation(hand):
    counts = [hand.count(x) for x in set(hand)]
    return Eval.index(sorted(counts))

def part1(hand):
     return evaluation(hand),[cards[False].index(i) for i in hand]

def part2(hand):
    if re.search('J',hand):
        maxvalue = (0,[0,0,0,0,0])
        for k in '23456789TQKA':
            tmphand = re.sub('J',k,hand)
            handval = (evaluation(tmphand),[cards[True].index(i) for i in hand])
            maxvalue = handval if handval > maxvalue else maxvalue
        return (maxvalue[0],maxvalue[1])

    return evaluation(hand),[cards[True].index(i) for i in hand]
    
def main(func):
    with open(ifile) as f:
            hand_evaluation = [parse_line(line.strip(),func) for line in f.readlines()]
    rankes = sorted(hand_evaluation, key = lambda x: (x[0][0], x[0][1]))
    return sum([(i+1)*bid[1] for i,bid in enumerate(rankes)])


if __name__ == '__main__':
    result1 = main(part1)
    print('Result 1:',result1)
    result2 = main(part2)
    print('Result 2:',result2)
