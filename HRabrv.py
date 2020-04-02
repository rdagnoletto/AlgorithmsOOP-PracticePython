#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    a_upper_only = ""
    a_lower_between = []
    a_upper_count = {}
    a_lower_count = {}
    b_count = {}
    ab_upper_diff = {}
    a_lower_extra = {}
    upper_chars = set()
    upper = True
    between = {}
    for c in a:
        if c.isupper():
            a_upper_count[c] = a_upper_count.get(c,0) + 1
            upper_chars.add(c)
            a_upper_only += c
            a_lower_between.append(between)
            if not upper:
                upper = True
                between = {}
        else:
            a_lower_count[c] = a_lower_count.get(c,0) + 1
            between[c] = between.get(c,0) + 1
            upper = False
    a_lower_between.append(between)
    
    for c in b:
        b_count[c] = b_count.get(c,0) +1
        upper_chars.add(c)

    for u in upper_chars:
        au = a_upper_count.get(u,0)
        bu = b_count.get(u,0)
        if au > bu:
            return "NO"
        ab_upper_diff[u] = bu - au

    for d in ab_upper_diff.keys():
        udiff = ab_upper_diff[d]
        alower = a_lower_count.get(str.lower(d),0)
        if udiff > alower:
            return "NO"
        a_lower_extra[str.lower(d)] = alower - udiff

    result = "YES"
    max_len = max(len(a),len(b))
    equal = len(a) == len(b)
    b_bigger = not equal and len(b) == max_len
    min_len = min(len(a),len(b))
    ib = 0
    if b_bigger:
        return "NO"
    diff = len(a) - len(b)
    for i in range(max_len):
        # print(i,ib, diff)
        if ib > min_len - 1:
            test = a[i:]
            if diff >= len(test) and test.islower():
                return "YES"
            else:
                return "NO"
        if a[i] == b[ib]:
            ib += 1
        elif str.upper(a[i]) == b[ib]:
            if i < max_len - 2 and ib < min_len -2:
                if a[i+1] == b[ib] and a[i+1] != b[ib+1] and diff > 0:
                    diff -= 1
                else:
                    ib += 1
            elif i < max_len - 2:
                for j in range(i,max_len):
                    if a[j].islower():
                        if diff == 0:
                            return "NO"
                        else:
                            diff -= 1
                    elif a[j] == b[ib]:
                        if diff == 0 or (len(a[j+1:]) == diff and a[j+1:].islower()):
                            return "YES"
                        else:
                            return "NO"
                    else:
                        return "NO"
            else:
                ib += 1
        else:
            if equal or a[i].isupper() or diff == 0:
                return "NO"
            else:
                diff -= 1
    return result
if __name__ == '__main__':
    with open('docs/HRabrv.txt', 'r') as myfile:
        # data = myfile.read()
        q = 10

        for q_itr in range(q):
            a = myfile.readline()

            b = myfile.readline()
            if q_itr == 3 or True:
                result = abbreviation(a, b)

                print(result)

