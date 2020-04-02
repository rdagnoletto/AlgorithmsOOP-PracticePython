#!/bin/python3

import math
import os
import random
import re
import sys
import time

def validPrefix(p):
    lp = p.split(" ")
    state = 0
    i = 0
    while i <len(lp):
        if state == 0:
            if lp[i] != "(":
                return False
            state = 1
            i += 1
        elif state ==1:
            if lp[i] != "+" and lp[i]!="*":
                return False
            state = 2
            i += 1
        elif state == 2:
            if lp[i].isdigit():
                state = 3
                i += 1
            elif lp[i] == "(":
                end = findClose(lp,i)
                if end != -1 and validPrefix(" ".join(lp[i:end+1])):
                    state = 3
                    i = end + 1
                else:
                    return False
            else:
                return False

        elif state == 3:
            if lp[i].isdigit():
                state = 4
                i += 1
            elif lp[i] == "(":
                end = findClose(lp,i)
                if end != -1 and validPrefix(" ".join(lp[i:end+1])):
                    state = 4
                    i = end + 1
                else:
                    return False

            else:
                return False
        elif state == 4:
            if lp[i]!= ")":
                return False
            if i != len(lp)-1:
                return False
            i += 1

    return True

def findClose(lp,i):
    rec_open = 1
    end = i
    for x in range(i+1,len(lp)):
        if lp[x] == "(":
            rec_open += 1
        elif lp[x] == ")":
            rec_open -=1
            if rec_open == 0:
                end = x
                break
    if end == i or rec_open != 0:
        return -1
    return end

def validPrefixStack(p):
    lp = p.split(" ")
    states = [0]
    stateTest = [["("],["+","*"],[],[],[")"]]
    for i,c in enumerate(lp):
        if states[-1] in [2,3]:
            if c.isdigit():
                states[-1] += 1
            elif c in stateTest[0]:
                states.append(1)
            else:
                return False
        elif c in stateTest[states[-1]]:
            states[-1] += 1
            if states[-1] > 4:
                states.pop()
                if len(states) > 0:
                    states[-1] += 1
                elif i != len(lp) -1:
                    return False
        else:
            return False

    if len(states) > 0:
        return False
    return True


def calcExpression(p):
    if not validPrefixStack(p):
        print("Invalid prefix expression")
        return None
    lp = p.split(" ")
    numbers = [[]]
    operations = []
    states = [0]
    stateTest = [["("],["+","*"],[],[],[")"]]
    for i,c in enumerate(lp):
        if states[-1] == 0:
            states[-1] += 1
        elif states[-1] == 1:
            operations.append(c)
            states[-1] += 1
        elif states[-1] in [2,3]:
            if c.isdigit():
                states[-1] += 1
                numbers[-1].append(int(c))
            else:
                states[-1] += 1
                states.append(1)
                numbers.append([])
        else:
            # print(states,numbers,operations)
            if operations[-1] == "*":
                result = numbers[-1][0]*numbers[-1][1]
            else:
                result = numbers[-1][0]+numbers[-1][1]
            states.pop()
            numbers.pop()
            operations.pop()
            if states:
                numbers[-1].append(result)
            else:
                return result





valid = ["( + 1 2 )", "( * 1 ( + 2 3 ) )",
        "( * ( + 1 2 ) ( + 3 40 ) )"]
        # 3, 5, 129

invalid = ["( + 1 2","( + 1 )","+ 1 2","(+ 1 ( + 2 3 )"]

print("Valid")
for p in valid:
    print(p,calcExpression(p))

print("Invalid")
for p in invalid:
    print(p,calcExpression(p))