import re

ifile = '2023/input/day1.txt'

WORDS = {'zero':'ze0ro','one':'o1ne','two':'t2wo','three':'th3ree','four':'fo4ur','five':'fi5ve','six':'si6x','seven':'sev7en','eight':'ei8ght','nine':'ni9ne'}


def get_number(X):
    b = [x for x in X if x.isdigit()]
    return int(b[0]+b[-1])

def get_number_with_text(X):
    for key,value in WORDS.items():
        X = re.sub(key,value,X)
    return get_number(X)


if __name__ == '__main__':
    with open(ifile) as file:
        line_result = [get_number(line) for line in file.readlines()]
        result_p1 = sum(line_result)

    with open(ifile) as file:
        line_result = [get_number_with_text(line) for line in file.readlines()]
        result_p2 = sum(line_result)
        
    print('Result Part1:', result_p1)
    print('Result Part2:', result_p2)
