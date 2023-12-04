import re

class Scratchcard:
    def __init__(self,id,win,guess):
        self.id = id
        self.win = win 
        self.guess = guess
    
    def check_win(self):
        for t in self.guess & self.win.keys():
            self.win[t] = 1

    def calc_score(self):
        a = sum(self.win.values())
        if a > 0:
            self.score = 2**(a-1)
            self.match = a
        else:
            self.score = 0
            self.match = 0

class Cardset:
    def __init__(self,cards):
        self.cards={i:{'card':c,'count':1} for i,c in enumerate(cards)}

    def check_cardset(self):
        setscore = 0
        for card in self.cards.keys():
            self.cards[card]['card'].check_win()
            self.cards[card]['card'].calc_score()
            setscore +=self.cards[card]['card'].score * self.cards[card]['count']

        self.score = setscore

    def win_copies(self):
        for i,card in self.cards.items(): 
            for n in range(i+1,i+card['card'].match+1):
                if n <= max(self.cards.keys()):
                    self.cards[n]['count'] += self.cards[i]['count']
                else:
                    continue

    def count(self):
        counts = 0
        for c in self.cards.values():
            counts += c['count']
        self.counts = counts


def parse_input(ifile):
    Cards=[]
    with open(ifile) as f:
        for line in f.readlines():
            A = line.split(':')
            cardid = re.search('\d*',A[0])
            B = A[1].split('|')
            win = re.findall('\d*',B[0])
            win = {int(w) : 0 for w in win if w.isnumeric()}
            guess = re.findall('\d*',B[1])
            guess = [int(g) for g in guess if g.isnumeric()]
            Cards.append(Scratchcard(cardid,win,guess))

    return Cardset(Cards)


def main():
    ifile = '2023/input/day4.txt'
    Tmp = parse_input(ifile)

    Tmp.check_cardset()
    result1 = Tmp.score

    Tmp = parse_input(ifile)
    Tmp.check_cardset()
    Tmp.win_copies()
    Tmp.count()
    result2 = Tmp.counts

    print(f"""2023 - Day4 
    Part 1: {result1}
    Part 2: {result2}""")
    
if __name__ == '__main__':
    main()