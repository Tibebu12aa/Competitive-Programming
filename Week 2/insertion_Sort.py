#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    lastelement=arr[-1]
    i= n-1
    while i>0 and arr[i-1] >lastelement:
        arr[i]=arr[i-1]
        print(*arr)
        i -= 1
    arr[i]=lastelement
    print(*arr)
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
