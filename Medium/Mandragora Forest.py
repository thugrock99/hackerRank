#!/bin/python3

import math
import os
import random
import re
import sys

#1. Using Greedy approach

# Complete the mandragora function below.
# First, Sort the array.
# Secondly, Eat the monsters with the lowest health points first until a certain point X.
#Why does this work? Consider the extreme cases:
#3a. We dont eat any monster: Then we only gain 1*(Health of all monsters) points.
#3b. We eat all monsters: Then we gain 0 points.
#Now 3b. is bad. 0 points is not good. But can we do better than a? yes, by already eating one monster, we have 2 strength and gain in total 2*(Health of all monsters - the weakest monster we ate).
#And so on... So you see that we improve by eating monsters. But can we improve forever? No! in 3b. we see that we gain 0 points when we eat all monsters. So the best solution is somewhere in the middle.
def mandragora(H):
    n     = len(H)
    total = sum(H)
    H.sort()
    s     = 1
    p     = total
    value = 0
    for i in range(n):
        #Eat the lower health one's one by one
        s+=1
        # Deduce the changes in total sum bcoz of eating this  and compute new value
        total-=H[i]
        value=total*s
        #Set the new value as P upto increasing sequence and once it start decreasing break the loop
        if value>p:
            p=value
        elif value<p:
            break
    return p

# 2. Using DP

def mandragora_DP(H):
    n     = len(H)
    H.sort()
    f = [0]*(n+1)
    for i in range(1,n+1):
        f[i]=f[i-1]+H[i-1]
    for i in range(1,n+1):
        if(i*(f[n]-f[i-1])>(i+1)*(f[n]-f[i])):
            return i*(f[n]-f[i-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        H = list(map(int, input().rstrip().split()))

        result = mandragora_DP(H)

        fptr.write(str(result) + '\n')

    fptr.close()
