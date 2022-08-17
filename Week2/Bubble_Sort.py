#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    numSwaps=0
    indexing_length = len(a) - 1 
    sorted = False 
    while not sorted:  
        sorted = True  
        for i in range(0, indexing_length): 
            if a[i]>a[i+1]:
                sorted = False 
                a[i], a[i+1] = a[i+1], a[i]
                numSwaps += 1
    print("Array is sorted in",numSwaps,"swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
    

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)