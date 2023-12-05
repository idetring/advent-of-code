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
                mappings[key].append(defrange(ints[0],ints[1],ints[2]))

    return (seeds,mappings)

def defrange(destination,source,rangelength):
    dest = range(destination,destination+rangelength)
    src = range(source,source+rangelength)
    return (dest,src)

def conversion(mappings,value):
    for m in mappings:
        if value in m[1]:
            diff =value - m[1].start if m[1].start != 0 else value
            k =  m[0].start + diff
            return k
    return value

def conversion_inv(mappings,value):
    for m in mappings:
        if value in m[0]:
            diff =value - m[0].start if m[0].start != 0 else value
            k =  m[1].start + diff
            return k
    return value

def conversionchain(mappings,value):
    chain = ['seed-to-soil','soil-to-fertilizer','fertilizer-to-water','water-to-light','light-to-temperature','temperature-to-humidity','humidity-to-location']
    for c in chain:
        value = conversion(mappings[c],value)
    return value

def conversionchain_inv(mappings,value):
    chain = ['seed-to-soil','soil-to-fertilizer','fertilizer-to-water','water-to-light','light-to-temperature','temperature-to-humidity','humidity-to-location']
    chain.reverse()
    for c in chain:
        value = conversion_inv(mappings[c],value)
    return value

def alternate(i):
    i = iter(i)
    while i:
        try:
            yield(next(i), next(i))
        except StopIteration:
            return

def main():

    seeds,mappings = parse_input(ifile)
    locations = [conversionchain(mappings,s) for s in seeds]
    result1=min(locations)

    ##

    result2=None

    print(f"""2023 - Day4 
    Part 1: {result1}
    Part 2: {result2}""")
    
if __name__ == '__main__':
    main()
