#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos   = 0
    neg   = 0
    zeros = 0
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
        else:
            zeros+=1
    pos = pos/len(arr)
    neg = neg/len(arr)
    zeros = zeros/len(arr)
    
    #different ways to set decimal or round in python
    print(str('%.6f'%pos),end='\n')
    print(str("{0:.6f}".format(neg)),end='\n')
    print(str(round(zeros,6)),end='\n')
   

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
 
