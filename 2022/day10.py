def main():
    ifile = '2022/input/day10.txt'

    CYCLE = {'noop':0,'addx':0}
    BREAKS = [20,60,100,140,180,220]

    def counter():
        """function to increase a counter"""
        counter=0
        def key():
            nonlocal counter
            counter+=1
            return counter
        return key


    values=[]

    with open(ifile,mode='r') as f:
        for line in f.readlines():
            line = line.replace('\n','').split(' ')
            for cycle in line:
                values.append(CYCLE.get(cycle) if cycle in CYCLE else int(cycle))

    SUM = 0
    for b in BREAKS:
        SUM += (sum(values[:b-1])+1)*b

    print(f"part_one: {SUM}")

    disp = ''

    for i,v in enumerate(values):
        X = (sum(values[:i])+1)
        I = i%40
        d = '#' if X in range(I-1,I+2) else '.'
        disp += d

    chunks = [disp[i:i+40] for i in range(0, len(disp), 40)]
    print(f"part_two:")
    for ch in chunks:
        print(ch)
    


if __name__ == '__main__':
    main()
