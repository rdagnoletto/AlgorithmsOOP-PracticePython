#!/bin/python3

import math
import os
import random
import re
import sys
import collections
from bisect import insort,bisect
from heapq import heappush, heappop, heapify  
import heapq

class MinHeap(object):
    def __init__(self, l = None): 
        if l is None:
            self.h = []
        else:
            heapify(l)
            self.h = l
    
    def heappush(self,x): heappush(self.h,x)
    def heappop(self): return heappop(self.h)
    def __getitem__(self,i): return self.h[i]
    def __len__(self): return len(self.h)
    # def delete(self, x):


class MaxHeap(MinHeap):
    def __init__(self, l = None): 
        if l is None:
            self.h = []
        else:
            l = [-i for i in l]
            heapify(l)
            self.h = l
    def heappush(self,x): heappush(self.h,-x)
    def heappop(self): return -heappop(self.h)
    def __getitem__(self,i): return -self.h[i]
# [2,5,3,7,5,8,9,3] n=8 O(n) O(n^2)
# [2,3,5]
def activityNotifications(expenditure, d):
    freq_min = dict()
    freq_max = dict()
    notif = 0
    even = False
    if d % 2 == 0:
        even = True

    init_trail = expenditure[:d]

    sortTrail = sorted(init_trail)
    max_heap_list, min_heap_list = sortTrail[:int(d/2)], sortTrail[int(d/2):]
    for m in max_heap_list:
        freq_max[m] = freq_max.get(m,0) + 1
    for m in min_heap_list:
        freq_min[m] = freq_min.get(m,0) + 1
    maxHeap = MaxHeap(max_heap_list)
    minHeap = MinHeap(min_heap_list)
    test = minHeap.__getitem__(0)
    if even:
        test = (test + maxHeap.__getitem__(0))/2
    if expenditure[d] >= 2*test:
        notif += 1

    min_deleted = 0
    max_deleted = 0
    for i in range(d+1,len(expenditure)):
        # sortTrail.remove(expenditure[i-(d+1)])
        old = expenditure[i-(d+1)]
        new = expenditure[i-1]
        max_add = False
        max_del = False
        if new <= maxHeap.__getitem__(0):
            maxHeap.heappush(new)
            freq_max[new] = freq_max.get(new,0) + 1
            max_add = True
        else:
            minHeap.heappush(new)
            freq_min[new] = freq_min.get(new,0) + 1
        
        if old <= maxHeap.__getitem__(0):
            freq_max[old] -= 1
            max_deleted += 1
            max_del = True
        else:
            freq_min[old] -= 1
            min_deleted += 1
        
        if max_del and not max_add:
            temp = minHeap.heappop()
            while freq_min[temp] == 0:
                temp = minHeap.heappop()
            freq_min[temp] -= 1
            maxHeap.heappush(temp)
            freq_max[temp] = freq_max.get(temp,0) + 1

        
        if max_add and not max_del:
            temp = maxHeap.heappop()
            while freq_max[temp] == 0:
                temp = maxHeap.heappop()
            freq_max[temp] -= 1
            minHeap.heappush(temp)
            freq_min[temp] = freq_min.get(temp,0) + 1


        test = minHeap.__getitem__(0)
        while freq_min[test] == 0:
            minHeap.heappop()
            test = minHeap.__getitem__(0)

        if even:
            test2 = maxHeap.__getitem__(0)
            while freq_max[test2] == 0:
                maxHeap.heappop()
                test2 = maxHeap.__getitem__(0)
            test = (test + test2)/2
        if expenditure[i] >= 2*test:
            notif += 1
        
    return notif
    
    
if __name__ == '__main__':
    with open('docs/HRnotifs.txt', 'r') as myfile:
        data = myfile.read()

        nd = data.split()

        n = int(nd[0])

        d = int(nd[1])

        expenditure = list(map(int, data.rstrip().split()))
        start = time.time()
        result = activityNotifications(expenditure, d)
        print(result)
        print("%d seconds" % int(time.time()-start))



