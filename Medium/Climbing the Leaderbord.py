#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    ls = [0]*(len(scores)+1)
    ls[0] = 1
    res =[0]*len(alice)
    for i in range(1,len(scores)):
        if scores[i]==scores[i-1]:
            ls[i] = ls[i-1]
        elif scores[i]<scores[i-1]:
            ls[i] = ls[i-1]+1
    idx = len(scores)-1
    for i in range(len(alice)):
        while idx>=0 and alice[i]>scores[idx]:
            idx-=1
        if idx==-1:
            res[i] = ls[0]
        elif alice[i]<scores[idx]:
            res[i] = ls[idx]+1
        else:
            res[i] = ls[idx]
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
 
