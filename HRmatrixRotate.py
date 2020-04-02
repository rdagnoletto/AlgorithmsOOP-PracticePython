#!/bin/python3

import math
import os
import random
import re
import sys

def newCoord(x,y,w,h,r):
    h += 1
    w += 1
    newX = x
    newY = y
    while r > 0:
        if (x == 0 and y != h-1) or (x == w-1 and y != 0):
            # move along y axis first
            if x == 0:
                if r > (h-1)-y:
                    newY = h-1
                    r -= (h-1)-y
                    y = newY
                else:
                    newY += r
                    r = 0
                    y = newY
            else:
                if r > y:
                    newY = 0
                    r -= y
                    y = newY
                else:
                    newY -= r
                    r = 0
                    y = newY
        else:
            if y == 0:
                if r > x:
                    newX = 0
                    r -= x
                    x = newX
                else:
                    newX -= r
                    r = 0
                    x = newX
            else:
                if r > (w-1)-x:
                    newX = w-1
                    r -= (w-1)-x
                    x = newX
                else:
                    newX += r
                    r = 0
                    x = newX
    return newX, newY

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    height = len(matrix) - 1
    width = len(matrix[0]) - 1
    testHeight = height
    testWidth = width
    numSquares = 1
    squarePerimeters = [2*(height+1) + 2*(width-1)]
    heights = [height]
    widths = [width]
    testHeight -= 2
    testWidth -= 2
    while testHeight > 0 and testWidth > 0:
        numSquares += 1
        squarePerimeters.append(2*(testHeight+1) + 2*(testWidth-1))
        heights.append(testHeight)
        widths.append(testWidth)
        testHeight -= 2
        testWidth -= 2
    print(squarePerimeters)
    print(heights)
    print(widths)
    for i,p in enumerate(squarePerimeters):
        ri = r
        if r == p:
            continue
        elif r > p:
            ri = r % p
            if ri == 0:
                continue
        startX = i
        startY = i
        # endX = startX + widths[i] -1 
        # endY = startY + heights[i] -1
        x = 0
        y = 0
        # if ri == 1:
        beginX = 0
        beginY = 0
        if p % ri == 0:
            z = int(p/ri)
            for c in range(ri):
                x, y = newCoord(0,0,widths[i],heights[i],c)
                temp = None
                for j in range(z):
                    nextX, nextY = newCoord(x,y,widths[i],heights[i],ri)
                    if temp is None:
                        temp = matrix[nextY+startY][nextX+startX]
                        matrix[nextY+startY][nextX+startX] = matrix[y+startY][x+startX]
                    else:
                        temp2 = matrix[nextY+startY][nextX+startX]
                        matrix[nextY+startY][nextX+startX] = temp
                        temp = temp2
                    x = nextX
                    y = nextY
        else:
            temp = None
            for j in range(p):
                nextX, nextY = newCoord(x,y,widths[i],heights[i],ri)

                if temp is None:
                    temp = matrix[nextY+startY][nextX+startX]
                    matrix[nextY+startY][nextX+startX] = matrix[y+startY][x+startX]
                else:
                    temp2 = matrix[nextY+startY][nextX+startX]
                    matrix[nextY+startY][nextX+startX] = temp
                    temp = temp2
                if nextX == beginX and nextY == beginY:
                    beginX, beginY = newCoord(nextX,nextY,widths[i],heights[i],1)
                    nextX = beginX
                    nextY = beginY
                    temp = None
                x = nextX
                y = nextY
                
    for i in range(height+1):
        line = ""
        for j in range(width+1):
            line += "%d " % matrix[i][j]
        print(line)

if __name__ == '__main__':
    with open('docs/HRmatrix.txt', 'r') as myfile:
        data = myfile.readline()

        mnr = data.rstrip().split()
        
        m = int(mnr[0])

        n = int(mnr[1])

        r = int(mnr[2])
        
        matrix = []
        for i in range(m):
            matrix.append(list(map(int, myfile.readline().rstrip().split())))
        # print(matrix)
    matrixRotation(matrix, r)
