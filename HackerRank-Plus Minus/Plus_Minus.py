#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    
    for i in range(len(arr)):
        if arr[i] > 0 :
            pos += 1
        elif arr[i] == 0:
            zer += 1
        else:
            neg += 1
            
    fractPos = pos / len(arr)
    fractNeg = neg / len(arr)
    fractZer = zer / len(arr)
    
    # here's the scale to six decimal places
    ratioPos = format(fractPos, '.6f')
    ratioNeg = format(fractNeg, '.6f')
    ratioZer = format(fractZer, '.6f')

    print(ratioPos)
    print(ratioNeg)
    print(ratioZer)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
