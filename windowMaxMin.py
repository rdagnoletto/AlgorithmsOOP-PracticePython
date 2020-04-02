import math
import os
import random
import re
import sys
import time

def riddle(arr):
    ans = []
    windows = []
    reduced = 0
    notRed = 0
    for w in range(1,len(arr)+1):
        if w == 1:
            ans.append(max(arr))
            windows.append(arr)
        elif w == len(arr):
            minfull = min(arr)
            ans.append(minfull)
            windows.append([minfull])
        else:
            maxmin = 0
            window = []
            found = False
            div = None
            # for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]:
            for i in [2, 3, 5, 7, 11, 13]:
                if not w%i:
                    found = True
                    div = i
                    break
            if found:
                reduced += 1
                test = windows[int(w/div - 1)]
                newW = int(w - w/div + 1)
            else:
                notRed +=1
                test = arr
                newW = w
                step = 1
            for i in range(len(test)-newW+1):
                minw = min(test[i:i+newW])
                window.append(minw)
                if minw > maxmin:
                    maxmin = minw
            ans.append(maxmin)
            windows.append(window)
    print(reduced,notRed)
    return ans


with open('docs/HRwindow.txt', 'r') as myfile:
    data = myfile.read()
    arr = list(map(int, data.rstrip().split()))

start = time.time()

res = riddle(arr)
# print(res)
print("%d seconds" % int(time.time()-start))
os.system('say "Finished"')