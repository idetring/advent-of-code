import numpy as np

class Node:
    def __init__(self,parent=None,position=None):
        self.parent     = parent 
        self.position   = position
        self.g          = 0
        self.h          = 0
        self.f          = 0

    def __eq__(self,other):
        return self.position == other.position

    def __repr__(self):
        out = f"""Node {self.position}\n   parent: {self.parent.position}\n   g,h,f = {self.g,self.h,self.f}\n"""
        return out

    def __contains__(self,item):
        return True if item == self.position else False


def main():
    data  = open("2022/input/day12.txt", "r", encoding="utf-8").read().splitlines()
    start = Node(None,[(i,d.find('S')) for i,d in enumerate(data) if 'S' in d][0])
    end  = Node(None,[(i,d.find('E')) for i,d in enumerate(data) if 'E' in d][0])
    df    = np.array([list(map(lambda x:ord(x) - ord('a'), [c for c in line])) for line in data])
    r,c = len(df),len(df[0])
    stepcost = 1
    df[start.position]=ord('a') - ord('a')
    df[end.position] = ord('z') - ord('a')

    open_nodes = [start,]
    closed_nodes = []

    outer_iterations = 0
    max_iterations = (r*c // 2) ** 10

    while open_nodes:
        outer_iterations += 1
        if outer_iterations > max_iterations:
            print("abort.... too many iterations...")
            return None

        current_node = open_nodes[0]
        current_index = 0
        for index, item in enumerate(open_nodes):
            if item.f < current_node.f:
                current_node = item
                current_index = index
                
        open_nodes.pop(current_index)
        closed_nodes.append(current_node)
        if len(closed_nodes)%1000 == 0:
            print(f"{len(closed_nodes)} cycles")
        if current_node == end:
            return return_path(current_node,df)

        children = make_nodes(current_node,closed_nodes,df,stepcost)

        for child in children:
            if child in closed_nodes:
                continue
            if len([i for i in open_nodes if child == i and child.f > i.f]) > 0:
                    continue
            open_nodes.append(child)

def return_path(current_node,maze):
    path = []
    no_rows, no_columns = np.shape(maze)
    # here we create the initialized result maze with -1 in every position
    result = [[-1 for i in range(no_columns)] for j in range(no_rows)]
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    path = path[::-1]
    start_value = 0
    for i in range(len(path)):
        result[path[i][0]][path[i][1]] = start_value
        start_value += 1
    return path
  
def get_adjacent_indices(ij, df):
    i,j = ij.position
    r,c = len(df),len(df[0])
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append(Node(ij,(i-1,j)))
    if i+1 < r:
        adjacent_indices.append(Node(ij,(i+1,j)))
    if j > 0:
        adjacent_indices.append(Node(ij,(i,j-1)))
    if j+1 < c:
        adjacent_indices.append(Node(ij,(i,j+1)))
    return adjacent_indices

def make_nodes(i,closed_nodes,elevation,stepcost):
    ## Make everything that has more elevation than 1 step unbearable for the algorithm
    neighbors = get_adjacent_indices(i,elevation)
    output = []
    ii,jj = i.position
    for ch in neighbors:
        if ch in closed_nodes:
            continue
        step =  elevation[ch.position] - elevation[ii,jj]
        ch.g = i.g + stepcost
        ch.h = step if step <= 1 else 999
        ch.f = ch.g + ch.h
        output.append(ch)
    return output


if __name__ == "__main__":
    a = main()
    print('part_one:')
    print(f"  path: {a}")
    print(f"  length of path: {len(a)-1}")
