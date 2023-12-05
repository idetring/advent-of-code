import re

DAY = '5'
YEAR = '2023'
ifile = f'{YEAR}/input/day{DAY}.txt'

def parse_input(ifile):
    mappings = {}
    with open(ifile) as f:
        seeds = [int(s) for s in re.findall('\d+',f.readline())]
        key=None
        for line in f.readlines():
            if re.search('\w+-\w+-\w+',line):
                key=re.search('\w+-\w+-\w+',line).group(0)
                mappings[key]=[]
                continue
            ints = [int(s) for s in re.findall('\d+',line)]
            if ints:
                mappings[key].append((ints[0],ints[1],ints[2])) # dest/src/sz

    return (seeds,mappings)

def map_value(mappings,value):
    for m in mappings:
        if value in range(m[1],m[1]+m[2]):
            newvalue = value - m[1] + m[0] 
            return newvalue 
    return value

def mapchain_value(mappings,value):
    chain = ['seed-to-soil','soil-to-fertilizer','fertilizer-to-water','water-to-light','light-to-temperature','temperature-to-humidity','humidity-to-location']
    for c in chain:
        value = map_value(mappings[c],value)
    return value


def map_ranges(mappings,ranges):
    A = []
    for m in mappings:
      src_end = m[1]+m[2]
      newranges = []
      while ranges:
        # [st                                     ed)
        #          [src       src_end]
        # [BEFORE ][INTER            ][AFTER        )
        (st,ed) = ranges.pop()
        # (src,sz) might cut (st,ed)
        before = (st,min(ed,m[1]))
        inter = (max(st, m[1]), min(src_end, ed))
        after = (max(src_end, st), ed)
        if before[1]>before[0]:
          newranges.append(before)
        if inter[1]>inter[0]:
          A.append((inter[0]-m[1]+m[0], inter[1]-m[1]+m[0]))
        if after[1]>after[0]:
          newranges.append(after)
      ranges = newranges
    return A+ranges

def mapchain_ranges(mappings,ranges):
    chain = ['seed-to-soil','soil-to-fertilizer','fertilizer-to-water','water-to-light','light-to-temperature','temperature-to-humidity','humidity-to-location']
    for c in chain:
        ranges = map_ranges(mappings[c],ranges)
    return ranges


def alternate(i):
    i = iter(i)
    while i:
        try:
            yield(next(i), next(i))
        except StopIteration:
            return

def main():

    seeds,mappings = parse_input(ifile)
    locations = [mapchain_value(mappings,s) for s in seeds]
    result1=min(locations)

    ##
    seeds,mappings = parse_input(ifile)
    seedsranges = [(a,b) for a,b in alternate(seeds)]
    part2 = []
    for sr in seedsranges:
        ranges = [(sr[0],sr[0]+sr[1])]
        locations = mapchain_ranges(mappings,ranges)
        part2.append(min(locations)[0])
    result2=min(part2)

    print(f"""2023 - Day4 
    Part 1: {result1}
    Part 2: {result2}""")
    
if __name__ == '__main__':
    main()
