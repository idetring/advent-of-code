ifile = '2023/input/day9.txt'

def calc_dif(n):
    return [n[i+1] - e for i,e in enumerate(n[:-1])]

def gen_pyramid(example):
    diff1 = example
    lists = [diff1,]
    while True:
        diff1 = calc_dif(diff1)
        lists.append(diff1)
        if all(d == 0 for d in diff1):
            break
    lists.reverse()
    return lists

def add_rightwards_(lists):
    """inplace adding"""
    lists[0].append(0)
    for i in range(1,len(lists)):
        lists[i].append(lists[i][-1] + lists[i-1][-1])

def add_leftwards_(lists):
    """inplace adding"""
    lists[0].insert(0,0)
    for i in range(1,len(lists)):
        lists[i].insert(0,lists[i][0] - lists[i-1][0])

def test():
    examples = [[0,3,6,9,12,15],[1,3,6,10,15,21],[10,13,16,21,30,45]]

    result_test1 = 0
    result_test2 = 0
    for example in examples:
        a = gen_pyramid(example)
        add_rightwards_(a)
        add_leftwards_(a)
        result_test1 += a[-1][-1]
        result_test2+= a[-1][0]
    return result_test1,result_test2

def main():
    result1 = 0
    result2 = 0
    with open(ifile) as f:
        for line in f.readlines():
            numbers = [int(n) for n in line.split()]
            a = gen_pyramid(numbers)
            add_rightwards_(a)
            add_leftwards_(a)
            result1 += a[-1][-1]
            result2 += a[-1][0]
    return result1,result2

if __name__ == '__main__':
    t1,t2 = test()
    print('Tests:',t1,t2)
    result1,result2 = main()
    print('Result Part1:',result1)
    print('Result Part2:',result2)
