#!/bin/python3

import math
import os
import random
import re
import sys
import time 

# Complete the countTriplets function below.
def countTriplets(arr, r):
    count = 0
    setarr = set(arr)
    if r == 1:
        for i in setarr:
            c = arr.count(i)
            if c >= 3:
                count += math.factorial(c)/(6*(math.factorial(c-3)))
        return int(count)
    
    # sarr = (list(setarr))
    trips = []
    for i in setarr:
        trip = [] 
        trip.append(i)
        if trip[0]*r in setarr:
            trip.append(trip[0]*r)
        else:
            continue
        if trip[0]*r*r in setarr:
            trip.append(trip[0]*r*r)
        else:
            continue
        trips.append(trip)
    # print(trips)
    countDict = dict()
    for i in arr:
        countDict[i] = countDict.get(i,0) + 1
    first = True
    for t in trips:
        arr2 = [i for i in arr if i in t]
        t0sums = [0]*len(arr2)
        t0sum = 0
        for i in range(len(arr2)):
            if arr2[i] == t[0]:
                t0sum += 1
            t0sums[i] = t0sum
        t2sums = [0]*len(arr2)
        t2sum = 0
        for i in range(len(arr2)-1,-1,-1):
            if arr2[i] == t[2]:
                t2sum += 1
            t2sums[i] = t2sum
        idx1list = [index for index, value in enumerate(arr2) if value == t[1]]
        idx0_start = arr2.index(t[0])
        idx0_end = len(arr2) - list(reversed(arr2)).index(t[0]) -  1
        idx2_start = arr2.index(t[2])
        idx2_end = len(arr2) - list(reversed(arr2)).index(t[2]) -  1
        if first:
            first = False
            print(t)
            print(arr2)
            print(idx1list)
            print(t0sums)
            print(t2sums)
        if idx1list[-1] < idx0_start or idx1list[0] > idx2_end or idx2_end < idx0_start:
            continue
        num = None
        num2 = None
        id1Dict = dict()
        for i1 in idx1list:
            if num is None:
                num = i1
                num2 = i1
                id1Dict[num] = 1
            elif i1 == num2+1:
                num2 += 1 
                id1Dict[num] += 1
            else:
                num = i1
                num2 = i1
                id1Dict[num] = 1

        for i1, val in id1Dict.items():
            if i1 < idx0_start or i1 > idx2_end:
                continue
            c = 1
            if i1 > idx0_end:
                c = c*countDict[t[0]]
            else:
                c = c*t0sums[i1]
            if i1 < idx2_start:
                c = c*countDict[t[2]]
            else:
                c = c*t2sums[i1]
            count += c*val
        # for i1 in idx1list:
        #     if i1 < idx0_start or i1 > idx2_end:
        #         continue
        #     c = 1
        #     if i1 > idx0_end:
        #         c = c*countDict[t[0]]
        #     else:
        #         c = c*(arr2[:i1].count(t[0]))
        #     if i1 < idx2_start:
        #         c = c*countDict[t[2]]
        #     else:
        #         c = c*(arr2[i1:].count(t[2]))
        #     count += c


    return int(count)

if __name__ == '__main__':

    with open('docs/HRtrips.txt', 'r') as myfile:
        data = myfile.read()
        # nr = input().rstrip().split()
        nr = data.rstrip().split()

        n = int(nr[0])

        r = int(nr[1])

        arr = list(map(int, data.rstrip().split()))
        start = time.time()
        ans = countTriplets(arr, r)
        print(time.time()-start)
        print(str(ans) + '\n')


