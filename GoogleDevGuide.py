#!/bin/python3

import math
import os
import random
import re
import sys
import time

def decompress(comp):
    stackNums = [1]
    stackStr = [""]
    # finalString = ""
    # foundFullNum = False
    openBrackets = 0
    partialNum = ""
    # partialString = ""
    for i,c in enumerate(comp):
        if c.isdigit():
            partialNum += c
        elif c == "[":
            openBrackets += 1
            stackNums.append(int(partialNum))
            stackStr.append("")
            partialNum = ""
        elif c.isalpha():
            stackStr[-1] += c
        elif c == "]":
            openBrackets -= 1
            decomp = stackStr.pop()*stackNums.pop()
            stackStr[-1] += decomp
    return stackStr[0]


def lakeVolumes(elevations):


    for i, e in enumerate(elevations):
        pass


testLake = [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]



# tests = ["3[abc]4[ab]c","10[a]","2[3[a]b]"]
# answers = ["abcabcabcababababc","aaaaaaaaaa","aaabaaab"]

# for i in range(len(tests)):
#     result = decompress(tests[i])
#     print(tests[i],result,answers[i],result == answers[i])