#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    n = len(arr)
    max_sums = [0]*(n)
    for i in range(n-1,-1,-1):
        if i == n-1:
            max_sums[i] = arr[i]
        elif i == n-2:
            if arr[i] > arr[i+1]:
                max_sums[i] = arr[i]
            else:
                max_sums[i] = max_sums[i+1]
        else:
            test = arr[i] + max(max_sums[i+2],0)
            if test > max_sums[i+1]:
                max_sums[i] = test
            else:
                max_sums[i] = max_sums[i+1]

    print(max_sums)
    print(max_sums[0])
    return max_sums[0]

if __name__ == '__main__':
    with open('docs/HRsubsum.txt', 'r') as myfile:
        data = myfile.read()
        n = 33196

        arr = list(map(int, data.rstrip().split()))

    res = maxSubsetSum(arr)




