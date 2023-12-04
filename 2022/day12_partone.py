import numpy as np
import math

def get_adjacent_indices(ij, df):
    i,j = ij
    r,c = len(df),len(df[0])
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < r:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < c:
        adjacent_indices.append((i,j+1))
    return adjacent_indices

def make_nodes(i,elevation):
    ## Make everything that has more elevation than 1 step unbearable for the algorithm
    neighbors = get_adjacent_indices(i,elevation)
    output = {}
    ii,jj = i
    for ch in neighbors:
        step = max(1,elevation[ch] - elevation[ii,jj])
        if step > 1:
            continue
        output[ch] = step
    return output

def make_nodes_part2(i,elevation):
    ## Make everything that has more elevation than 1 step unbearable for the algorithm
    neighbors = get_adjacent_indices(i,elevation)
    output = {}
    ii,jj = i
    for ch in neighbors:
        step = max(1,elevation[ii,jj] -  elevation[ch])
        if step > 1:
            continue
        output[ch] = step
    return output

def make_graph(df,part):
    graph = {}
    r,c = df.shape
    for rr in range(r):
        for cc in range(c):
            graph[(rr,cc)] = part((rr,cc),df) 

    return graph

def main(part):
    data  = open("2022/input/day12.txt", "r", encoding="utf-8").read().splitlines()
    start = [(i,d.find('S')) for i,d in enumerate(data) if 'S' in d][0]
    end   = [(i,d.find('E')) for i,d in enumerate(data) if 'E' in d][0]
    df    = np.array([list(map(lambda x:ord(x) -97, [c for c in line])) for line in data])
    df[start]=ord('a') - 97
    df[end] = ord('z') - 97

    
    Graph = make_graph(df,part)

    open_nodes = Graph
    shortest_distances = {}
    path = []
    path_nodes = {}

    for nodes in open_nodes:
        shortest_distances[nodes] = 100_000
    shortest_distances[start] = 0

    while open_nodes:
        min_node = None
        for current_node in open_nodes:
            if min_node is None:
                min_node = current_node
            elif shortest_distances[min_node] > shortest_distances[current_node]:
                min_node = current_node
        for node,value in open_nodes[min_node].items():
            if value + shortest_distances[min_node] < shortest_distances[node]:
                shortest_distances[node] = value + shortest_distances[min_node]
                path_nodes[node] = min_node

        open_nodes.pop(min_node)

    node = end
    while node != start:
        try :
            path.insert(0,node)
            node = path_nodes[node]
        except Exception:
            print('Path not possible')
            break
    path.insert(0,start)

    return path


def main2(part):
    data  = open("2022/input/day12test.txt", "r", encoding="utf-8").read().splitlines()
    end = [(i,d.find('S')) for i,d in enumerate(data) if 'S' in d][0]
    start   = [(i,d.find('E')) for i,d in enumerate(data) if 'E' in d][0]
    df    = np.array([list(map(lambda x:ord(x) -97, [c for c in line])) for line in data])
    df[start]=ord('z') - 97
    df[end] = ord('a') - 97

    Graph = make_graph(df,part)

    open_nodes = Graph
    shortest_distances = {}
    path = []
    path_nodes = {}

    for nodes in open_nodes:
        shortest_distances[nodes] = math.inf
    shortest_distances[start] = 0

    while open_nodes:
        min_node = None
        for current_node in open_nodes:
            if min_node is None:
                min_node = current_node
            elif shortest_distances[min_node] > shortest_distances[current_node]:
                min_node = current_node
        if not open_nodes[min_node]: break;

        for node,value in open_nodes[min_node].items():
            if value + shortest_distances[min_node] < shortest_distances[node]:
                shortest_distances[node] = value + shortest_distances[min_node]
                path_nodes[node] = min_node

        open_nodes.pop(min_node)

    node = end
    while node != start:
        try :
            path.insert(0,node)
            node = path_nodes[node]
        except Exception:
            print('Path not possible')
            break
    path.insert(0,start)

    return path




if __name__ == "__main__":
    a = main2(make_nodes_part2)
    print('part_one:')
    print(f"  path: {a}")
    print(f"  length of path: {len(a)-1}")

    b = main2(make_nodes_part2)
    print('part_two:')
    print(f"  path: {b}")
    print(f"  length of path: {len(b)-1}")