import numpy as np

data = open("2021/input/day7.txt", encoding='utf-8').read()
df = np.array([int(x) for x in data.split(",")])

p_min,p_max = min(df),max(df)

# PART 1
fuels = [sum([abs(x - i) for x in df]) for i in range(p_max)]

# PART 2
def linear_increase(n):
    return (n * (n+1))/2

fuels = [sum([linear_increase(abs(x - i)) for x in df]) for i in range(p_max)]
