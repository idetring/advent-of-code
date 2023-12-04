MOVES = {'L':(-1,0),'R':(1,0),'U':(0,1),'D':(0,-1)}

import operator
import numpy as np

def gradient2d(dif): 
    return [(int(x/abs(x)) if x != 0 else 0) for x in dif]

def listoper(func,A,B):
    return [func(x,y) for x,y in zip(A,B)]

def check_for_move(dif):
    return min(dif) < -1 or max(dif) > 1

def make_a_move(T,dif):
    dif_new = gradient2d(dif)
    return listoper(operator.add,T,dif_new)

def main(rlength=1):
    H = [0,0]
    T = [[0,0]]*rlength

    # 1.
    # 1.1 Make baby step with H 
    T_pos = []
    T_pos.append(T[-1])

    with open('2022/input/day9.txt') as f:
        for line in f.readlines():
            d,n = line.replace('\n','').split(' ')
            for _ in range(int(n)):
                H = listoper(operator.add,H,MOVES[d])
                # 1.2. calc diff of H and T
                h = H
                for i,t in enumerate(T):
                    dif = listoper(operator.sub,h,t)
                    # 1.3. check if T is adjacent ot H
                    move = check_for_move(dif)
                    T[i] = make_a_move(t,dif) if move else T[i]
                    h = T[i]

                T_pos.append(T[-1])


    T_pos = list(set([ tuple(t) for t in T_pos ]))
    return len(T_pos)


if __name__ == "__main__":
    print(f"part_one: {main(rlength=1)}")
    print(f"part_two: {main(rlength=9)}")

