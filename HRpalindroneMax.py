#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    odd = False
    middle = None
    if n % 2 != 0:
        odd = True
    stack = []
    sList = list(s)
    for _ in range(int(n/2)):
        stack.append(sList.pop())
    if odd:
        middle = sList.pop()

    diff = 0
    for i in range(int(n/2)):
        if stack[i] != sList[i]:
            diff += 1
    if k < diff:
        return "-1"
    extra = k-diff
  
    for i in range(int(n/2)):
        if stack[i] != sList[i]:
            maxTemp = max(stack[i],sList[i])
            if extra == 0 or maxTemp == '9':
                stack[i] = maxTemp
                sList[i] = maxTemp
                k -= 1
            else:
                stack[i] = '9'
                sList[i] = '9'
                extra -= 1
                k -= 2
        else:
            if extra >= 2 and sList[i] != '9':
                stack[i] = '9'
                sList[i] = '9'
                extra -= 2
                k -= 2 
        
    if k > 1:
        for i in range(int(n/2)):
            if sList[i] != '9':
                sList[i] = '9'
                stack[i] = '9'
                k -= 2
                if k <= 1:
                    break
    if odd:
        if k >= 1 and middle != '9':
            middle = '9'
            k -= 1
        sList.append(middle)
    
    for _ in range(int(n/2)):
        sList.append(stack.pop())
    
    return ''.join(sList)


if __name__ == '__main__':
    with open('docs/HRpal.txt', 'r') as myfile:
        data = myfile.read()

        nk = data.split()

        n = int(nk[0])

        k = int(nk[1])

        s = data

        result = highestValuePalindrome(s, n, k)
        print(result)

    
