import re

Abs_number = 0 

def check(symbols,digits,Abs_number):
    for s in symbols:
        for d in digits:
            si = s.start(),s.end()
            di = d.start(),d.end()
            if (si[0] >= di[0]-1) and (si[1] <= di[1]+1):
                Abs_number += int(d.group(0))
    return Abs_number

Allsymbols=[]
with open('2023/input/day3.txt') as f:
    all = f.read()
[Allsymbols.append(x) for x in all if not x.isnumeric() and x not in ['.','\n','n']]
Allsymbols=set(Allsymbols)
Sym='['+','.join(Allsymbols)+']'

Abs_number = 0 
with open('2023/input/day3.txt') as f:
    symbols_old = []
    digits_old = []
    for line in f.readlines():
        symbols_new = list(re.finditer(Sym,line))
        digits_new = list(re.finditer('\d+',line))
        Abs_number = check(symbols_new,digits_new,Abs_number)
        Abs_number = check(symbols_new,digits_old,Abs_number)
        Abs_number = check(symbols_old,digits_new,Abs_number)
        symbols_old = symbols_new
        digits_old = digits_new

print('Part1:',Abs_number)

Abs_number = 0 

def check2(symbols,digits,Abs_number):
    for s in symbols:
        count = 0
        numbers = []
        for d in digits:
            si = s.start(),s.end()
            di = d.start(),d.end()
            if (si[0] >= di[0]-1) and (si[1] <= di[1]+1):
                count += 1 
                numbers.append(int(d.group(0)))
        if count == 2:
            Abs_number += numbers[0] * numbers[1]
    return Abs_number

Sym='[*]'

Abs_number = 0 
with open('2023/input/day3.txt') as f:    
    digits_veryold = []
    digits_old = []
    digits_new = []
    symbols_old = []
    symbols_new = []
    for line in f.readlines():
        symbols = list(re.finditer(Sym,line))
        digits_new = list(re.finditer('\d+',line))
        Abs_number = check2(symbols_old,digits_veryold+digits_old+digits_new,Abs_number)
        digits_veryold = digits_old
        digits_old = digits_new
        symbols_old = symbols

    Abs_number = check2(symbols_old,digits_old+digits_new,Abs_number)

print('Part2:',Abs_number)
