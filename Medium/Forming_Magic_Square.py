#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    # The pattern [1,6,7,2,9,4,3,8] is common pattern we can observe in all 8 magic square combinations of 3*3
    #  Consider Given array traversed as : (Starting from [0,1] ans ending at [0][0] i.e covering all elements except 5         
    #          ----->------
    #   | 00      01    02 |
    #   | 10      11    12 |
    #   | 20      21    22 |
    #   --------<-----------
    #   Points to be Noted:
    #   1. 5 is always at the center of 3*3 magic square
    #   2. Even Numbers(2,4,6,8) can only be present at corners
    #   3. Only odd numbers(1,3,7,9) can be present in edge position except 5
    #
    # Patterns possible for magic square if we traverse in above specified way
    # As Only odd numbers can present in edge positionlike[0,1] we take all 1,3,7,9 and write patterns in clock wise order
    p1 = [6,7,2,9,4,3,8] #for 1 as in [0][1]
    p2 = [2,9,4,3,8,1,6] #for 7 as in [0][1]
    p3 = [4,3,8,1,6,7,2] #for 9 as in [0][1]
    p4 = [8,1,6,7,2,9,4] #for 3 as in [0][1]
    
    # Traversing the given square in same way
    s1 = [s[0][2],s[1][2],s[2][2],s[2][1],s[2][0],s[1][0],s[0][0]]
    
    # Compute Costs
    c1=abs(1-s[0][1])+cost(s1,p1)
    c2=abs(7-s[0][1])+cost(s1,p2)
    c3=abs(9-s[0][1])+cost(s1,p3)
    c4=abs(3-s[0][1])+cost(s1,p4)
    
    # Return min Const out of C1,C2,C3,C4 and 
    # |5-s[1][1]| as it is always compulsory to replace center of matrix with 5 for any magic square
    return min(min(min(c1,c2),c3),c4)+abs(5-s[1][1])

# Calculate cost of given magic square pattern(and its reflection too) with given array
def cost(s,p):
    cost=0
    cost_rev = 0
    for i in range(7):
        cost =  cost+abs(s[i]-p[i])
        cost_rev = cost_rev+abs(s[i]-p[6-i])
    return min(cost,cost_rev)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
 
