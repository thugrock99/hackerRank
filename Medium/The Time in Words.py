#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    nums = ["zero", "one", "two", "three", "four", 
            "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", 
            "fourteen", "fifteen", "sixteen",  
            "seventeen", "eighteen", "nineteen",  
            "twenty", "twenty one", "twenty two",  
            "twenty three", "twenty four",  
            "twenty five", "twenty six", "twenty seven", 
            "twenty eight", "twenty nine"]
  
    if (m == 0): 
        return nums[h]+ " o' clock" 
  
    elif (m == 1): 
        return "one minute past "+nums[h]
  
    elif (m == 59): 
        return "one minute to "+nums[(h % 12) + 1]
  
    elif (m == 15): 
        return "quarter past "+nums[h]
  
    elif (m == 30): 
        return "half past "+nums[h] 
  
    elif (m == 45): 
        return "quarter to "+nums[(h % 12) + 1] 
  
    elif (m <= 30): 
        return nums[m]+" minutes past "+nums[h] 
  
    elif (m > 30): 
        return nums[60 - m]+ " minutes to "+nums[(h % 12) + 1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
 
