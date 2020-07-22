#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    n = len(container)
    if n==1:
        return 'Possible'
    row_sum = [0]*n
    col_sum = [0]*n
    for i in range(n):
        row_sum[i] = sum(container[i])
        val = 0
        for j in range(n):
            val += container[j][i]
        col_sum[i] = val
    row_sum.sort()
    col_sum.sort()
    for i in range(n):
        if row_sum[i]!=col_sum[i]:
            return 'Impossible'
    return 'Possible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
 
