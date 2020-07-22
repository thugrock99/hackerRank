#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A,H,W):

    surfaces = 0
    for i in range(H):
        for j in range(W):
            surfaces += 2  # For Top and Bottom sides
            if i-1==-1:                           # for each side of all 4 sides
                surfaces += A[i][j]
            elif A[i-1][j]<A[i][j]:
                surfaces += (A[i][j]-A[i-1][j])

            if i+1==H:
                surfaces += A[i][j]
            elif A[i+1][j]<A[i][j]:
                surfaces += (A[i][j]-A[i+1][j])

            if j-1==-1:
                surfaces += A[i][j]
            elif A[i][j-1]<A[i][j]:
                surfaces += (A[i][j]-A[i][j-1])

            if j+1==W:
                surfaces += A[i][j]
            elif A[i][j+1]<A[i][j]:
                surfaces += (A[i][j]-A[i][j+1])

    return surfaces
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A,H,W)

    fptr.write(str(result) + '\n')

    fptr.close()
 
