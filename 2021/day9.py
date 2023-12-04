import numpy as np

ifile = '2021/input/day9.txt'


from scipy import ndimage

data = open(ifile, "r", encoding="utf-8").read()
df = np.array([list(map(int, [c for c in line])) for line in data.splitlines()])

kernel = np.array([[0,1,0],[1,0,1],[0,1,0]])
kernel_indices = (np.array([0, 1, 1, 2]), np.array([1, 0, 2, 1]))


def convolution(matrix, kernel):
    ConSum = 0
    # kernel can be asymmetric but still needs to be odd
    k_height, k_width = kernel.shape
    m_height, m_width = matrix.shape
    padded = np.pad(matrix, (1, 1),constant_values=10)

    # iterates through matrix, applies kernel, and sums
    for i in range(m_height):
        for j in range(m_width):
            between = padded[i:k_height+i, j:k_width+j]*kernel
            ConSum += 1+padded[i+1][j+1] if np.min(between[kernel_indices]) > padded[i+1][1+j] else 0

    return ConSum




import collections
def maxAreaOfBasin(grid):
    """
    :type grid: List[List[int]] or np.array
    :rtype: int
    """
    r, c =  len(grid), len(grid[0])
    finished = collections.defaultdict(int)
    res_ = {finished[(i,j)] for i in range(r)
                        for j in range(c) if grid[i][j] == 9}

    def dfs(i,j):
        open_list.append((i,j))
        while open_list:
            i,j = open_list.pop()
            finished[(i,j)]
            close_list.append((i,j))
            temp = [(m,n) for m,n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if m>=0 and m<r and n>=0 and n<c and grid[m][n] < 9]
            if temp:
                for item in temp:
                    if item not in open_list and item not in close_list:
                        open_list.append(item)
        res_.add(len(close_list))#sum([df[x] for x in close_list]))
    for i in range(r):
        for j in range(c):
            if (i,j) not in finished:
                open_list = []
                close_list = []
                dfs(i,j)
    return sorted(res_,reverse=True)


if __name__ == "__main__()":
    print(True)
    partone = convolution(df,kernel)
    print(f'result of part one: {partone:.>20}')
    Areas = maxAreaOfBasin(df)
    parttwo = Areas[0]*Areas[1]*Areas[2]
    print(f'result of part two: {parttwo:.>20}')
