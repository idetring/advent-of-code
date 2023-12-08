import re

DAY = '6'
YEAR = '2023'
ifile = f'{YEAR}/input/day{DAY}.txt'

def parse_input(ifile):
    with open(ifile) as f:
        time = [int(s) for s in re.findall('\d+',f.readline())]
        distance = [int(s) for s in re.findall('\d+',f.readline())]

    return (time,distance)

def check_race(time,distance):
    wins = 0
    timehold = 1
    while timehold < time:
        racedist = timehold*(time-timehold)
        if racedist > distance:
            wins += 1
        timehold += 1
    return wins


def main():

    times, distances = parse_input(ifile)
    result1 = 1
    for t,d in zip(times,distances):
        result1 *= check_race(t,d)
    result2 = None

    ## Part2 
    time = int(''.join([str(t) for t in times]))
    distance = int(''.join([str(d) for d in distances]))

    distances = [timecharged * (time - timecharged) for timecharged in range(time)]
    result2 = sum([1 for d in distances if d > distance])

    print(f"""2023 - Day4 
    Part 1: {result1}
    Part 2: {result2}""")
    
if __name__ == '__main__':
    main()
