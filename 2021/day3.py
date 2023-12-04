from dataclasses import dataclass

@dataclass
class Energy:
    gamma = ''
    epsilon = ''
    co2 = ''
    o2 = ''


class Lognote:
    def __init__(self,num):
        self.N = 0
        for i in range(num):
            setattr(self,str(i),0)

a = Lognote(12)
with open('2021/input/day3.txt') as f:
    for line in f.readlines():
        line = line.replace('\n','')
        a.N += 1
        for i,b in enumerate(line):
            setattr(a,str(i),getattr(a,str(i))+int(b))


power = Energy()
for i in range(12):
    G = getattr(a,str(i))*2 > a.N
    power.gamma = power.gamma + '1' if G else power.gamma + '0'
    power.epsilon = power.epsilon + '0' if G else power.epsilon + '1'


consumption = int(power.gamma,2) * int(power.epsilon,2)


with open('2021/input/day3.txt') as f:
    out = [line.replace('\n','') for line in f.readlines()]


def count_numbers(IN,pos):
    tmp = [int(x[pos]) for x in IN]
    return str(round(sum(tmp)/len(tmp)))

pos = 0
while len(out) > 5:
    out = list(filter(lambda x:(x[pos] == count_numbers(out,pos)),out))
    pos += 1

power.o2=out[0]

out = ''
with open('2021/input/day3.txt') as f:
    out = [line.replace('\n','') for line in f.readlines()]

pos = 0
while len(out) > 1:
    out = list(filter(lambda x:(x[pos] != count_numbers(out,pos)),out))
    pos += 1

power.co2 = out[0]


oxygen = int(power.co2,2) * int(power.o2,2)
