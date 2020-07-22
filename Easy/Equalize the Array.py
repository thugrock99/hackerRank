#!/bin/python3

import math
import os
import random
import re
import sys
import collections
# Complete the equalizeArray function below.
def equalizeArray(arr):
    counter = collections.Counter(arr)
    mx = 0
    for key in counter:
        if counter[key]>mx:
            mx = counter[key]
    return len(arr)-mx
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
 
