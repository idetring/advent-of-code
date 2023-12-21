import re

ifile = '2023/input/day19.txt'

# command = {var<cond:goto,...,goto}
# workflow in -> ... -> A/R
# set start  
# loop through parts
    
class Condition():
    def __init__(self,condition):
        self.raw = condition
        self.condition = f"{condition['left']} {condition['oper']} {condition['right']}" 
        self.goto = condition['goto']

    def evaluate(self,state):
        x,m,a,s = state['x'], state['m'], state['a'], state['s']
        if eval(self.condition):
            return self.goto

#Conditions = Condition('True' if A/R)
condition_regex = re.compile(
    r"(?P<left>\w+)(?P<oper>>|<)(?P<right>\w+):(?P<goto>\w+)"
)

def parse_input(ifile):
    DB = {} 
    with open(ifile) as f:
        data = f.read()
    conds, paths = data.split('\n\n')
    for c in conds.split('\n'):
        name = c.split("{")[0]
        conditions = c.split("{")[1].split("}")[0].split(",")
        DB[name] = []
        for cc in conditions:
            condmatch = condition_regex.match(cc)
            if condmatch:
                DB[name].append(Condition(condmatch.groupdict()))
            else:
                DB[name].append(Condition({'left':'1','oper':'<','right':'4001','goto':cc}))
    Rules = []
    for p in paths.split('\n'):
        vars = re.findall('[xmas]',p)
        nums = re.findall('\d+',p)
        Rules.append({})
        for v,n in zip(vars,nums):
            Rules[-1][v] = int(n)
    
    result1 = 0
    for rule in Rules:
        k = 'in'
        while k:
            c = [c.evaluate(rule) for c in DB[k]]
            k = next(item for item in c if item is not None)
        result1 += sum(rule.values()) if k == 'A' else 0


    result2 = 0 
    for rule in Rules:
        k = ['in']
    return result1 

if __name__ == '__main__':
    result1 = parse_input(ifile)
    print(result1)