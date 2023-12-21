import numpy as np

ifile = '2023/input/day21.txt'

def get_adjacent_nodes(ij, df):
    i,j = ij
    r,c = len(df),len(df[0])
    adjacent_indices = []
    if i > 0 and df[i-1,j]:
        adjacent_indices.append((i-1,j))
    if i+1 < r and df[i+1,j]:
        adjacent_indices.append((i+1,j))
    if j > 0 and df[i,j-1]:
        adjacent_indices.append((i,j-1))
    if j+1 < c and df[i,j+1]:
        adjacent_indices.append((i,j+1))
    return adjacent_indices

def make_nodes(i,elevation):
    ## Make everything that has more elevation than 1 step unbearable for the algorithm
    neighbors = get_adjacent_nodes(i,elevation)
    output = []
    ii,jj = i
    for ch in neighbors:
        output.append(ch)
    return output

def parse_file(ifile):
    data  = open(ifile, "r", encoding="utf-8").read().splitlines()
    start = [(i,d.find('S')) for i,d in enumerate(data) if 'S' in d]
    df    = np.array([list(map(lambda x: 1 if x in '.S' else 0, [c for c in line])) for line in data])
    return df, start[0]

def main(ifile):
    result1,result2 = 0,0    
    df, start = parse_file(ifile)

    max_iterations = 64
    outer_iterations = 0
    open_nodes = [start,]

    while open_nodes:
        outer_iterations += 1
        if outer_iterations > max_iterations:
            print("abort.... iterations reached...")
            result1 = len(open_nodes)
            break
        next_nodes = []
        for item in open_nodes:            
            next_nodes += make_nodes(item,df)

        open_nodes = set(next_nodes)

    outer_iterations = 0
    open_nodes = [start,]
    len_nodes = [1]

    while open_nodes:
        outer_iterations += 1
        if len_nodes[-2:] == len_nodes[-4:-2]:
            print("abort.... iterations reached...")
            result2 = len_nodes
            break
        next_nodes = []
        for item in open_nodes:            
            next_nodes += make_nodes(item,df)

        open_nodes = set(next_nodes)
        len_nodes.append(len(open_nodes))


    return result1, result2


if __name__ == "__main__":
    result1, result2 = main(ifile)
    print(result1,result2)
    print(len(result2))