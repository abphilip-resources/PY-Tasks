from itertools import product

def solve(s):
    for (row, col) in product(range(0,9), repeat=2):
        if s[row][col] == 0:
            for num in range(1,10):
                k = True 
                for i in range(0,9):
                    if (s[i][col] == num) or (s[row][i] == num): 
                        k = False; break
                for (i, j) in product(range(0,3), repeat=2):
                    if s[row-row%3+i][col-col%3+j] == num: 
                        k = False; break
                if k:       
                    s[row][col] = num
                    if trial := solve(s): return trial
                    else: s[row][col] = 0
            return False 
    return s

def display(s):
    s = [['*' if z == 0 else z for z in row] for row in s]
    print()
    for row in range(0,9):
        if ((row % 3 == 0) and (row != 0)): print('-'*33) 
        for col in range(0,9):
            if ((col % 3 == 0) and (col != 0)):
                print(' | ', end='') 
            print('', s[row][col], '', end='')
        print()
    print()
       
s = [[5,3,0,0,7,0,0,0,0],
     [6,0,0,1,9,5,0,0,0],
     [0,9,8,0,0,0,0,6,0],
     [8,0,0,0,6,0,0,0,3],
     [4,0,0,8,0,3,0,0,1],
     [7,0,0,0,2,0,0,0,6],
     [0,6,0,0,0,0,2,8,0],
     [0,0,0,4,1,9,0,0,5],
     [0,0,0,0,8,0,0,7,9]]

display(s)
display(solve(s))