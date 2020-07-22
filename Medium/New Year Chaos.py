#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    swap=0
    while True:
        count = 0
        initial = swap
        for i in range(len(q)-1):
            if(q[i]>q[i+1]):
                temp   = q[i+1]
                q[i+1] = q[i]
                q[i]   = temp

                swap = swap +1
                count = count+1
            else:
                count =0
            if(count>2):
                return "Too chaotic"
        if(initial==swap):
            return swap
    return -1

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
 
