#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = "".join(s.split())
    n = len(s)
    ls = list(s)
    cl = math.ceil(math.sqrt(n))
    for i in range(cl):
        j=i
        while j<n:
            print(ls[j],end="")
            j+=cl
        print("",end=" ")            


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    #result = encryption(s)
    encryption(s)
    #fptr.write(result + '\n')

    #fptr.close()
 
