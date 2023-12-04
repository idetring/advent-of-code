ifile = '2022/input/day6.txt'

def detect_first(data,num):
    for i,e in enumerate(range(num,len(data))):
        if len(set(data[i:e])) == num:
            break
    return e

if __name__ == "__main__()":
    data = open(ifile).read()
    res1,res2 = detect_first(data,4),detect_first(data,14)
    print(f'result part one: {res1:.>10}')
    print(f'result part two: {res2:.>10}')
