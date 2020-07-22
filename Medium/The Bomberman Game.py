#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def bomberMan(n, grid):
    if n==1:
        print('\n'.join(map(''.join,grid)))
        return
    if n%2==0:
        r = len(grid)
        c = len(grid[0])
        s = ''.ljust(c,chr(79))
        print ('\n'.join(map(''.join,[s]*r)))
        return
    r = len(grid)
    c = len(grid[0])
    third = []
    fifth = []
    for i in range(r+2):
        ls = []
        for j in range(c+2):
            ls.append(0)
        third.append(ls)
    for i in range(r+2):
        ls = []
        for j in range(c+2):
            ls.append(0)
        fifth.append(ls)
    for i in range(1,r+1):
        for j in range(1,c+1):
            if grid[i-1][j-1]==chr(79):
                third[i][j] = third[i-1][j]= third[i+1][j] = third[i][j-1] = third[i][j+1]=1
    if (n+1)%4==0:     
        for i in range(1,r+1):
            for j in range(1,c+1):
                if third[i][j]==1:
                    print('.',end='')
                else:
                    print(chr(79),end='')
            print('',end='\n')
    for i in range(1,r+1):
        for j in range(1,c+1):
            if third[i][j]==0:
                fifth[i][j] =  fifth[i-1][j] = fifth[i+1][j] = fifth[i][j-1] = fifth[i][j+1] =1
    if (n-1)%4==0:
        for i in range(1,r+1):
            for j in range(1,c+1):
                if fifth[i][j]==1:
                    print('.',end='')
                else:
                    print(chr(79),end='')
            print('',end='\n')

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(list(str(grid_item)))

    bomberMan(n, grid)

    #fptr.write('\n'.join(result))
    #fptr.write('\n')

    #fptr.close()
