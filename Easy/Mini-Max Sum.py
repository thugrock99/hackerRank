#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    s = sum(arr)
    mi = min(arr)
    ma = max(arr)
    print(str(s-ma)+" "+str(s-mi),end="")

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
 
