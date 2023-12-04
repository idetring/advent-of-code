Prio = "abcdefghijklmnopqrstuvwxyz"
Prios = {}
for x in Prio:
    Prios[x] = (ord(x) - 96)
    Prios[x.upper()] = ord(x.upper()) - 38

out = ""
with open("2022/input/day3.txt") as f:
    for line in f.readlines():
        out += day3(line)


def day3(line):
    line = line.replace("\n","")
    n = len(line)
    a = line[:n//2]
    b = line[n//2:]
    out = [aa for aa in a if aa in b]
    return out[0]

Priosum = sum([Prios[x] for x in out])



def define_group():
    counter=0
    N=0
    linecount =counting()
    def key(line):
        N = linecount()
        nonlocal counter
        if N%3 == 0:
            counter+=1
        return counter
    return key

def counting():
    counter=-1
    def key():
        nonlocal counter
        counter+=1
        return counter
    return key


from itertools import groupby
out = ''
with open("2022/input/day3.txt") as f:
    for key,group in groupby(f,key=define_group()):
        A= [g.replace('\n','') for g in group]
        out += [aa for aa in A[0] if aa in A[1] and aa in A[2]][0]

Priosum = sum([Prios[x] for x in out])
