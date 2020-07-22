#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    ls = [0]*k
    if k==1:
        return 1
    for i in s:
        ls[i%k] += 1
    count = 0
    if ls[0]!=0:
        count += 1
    for i in range(1,k//2):
        count += max(ls[i],ls[k-i])

    if k%2==0 and ls[k//2]!=0:
        count+=1
    elif k%2==1:
        count += max(ls[k//2],ls[k//2+1])
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
 
