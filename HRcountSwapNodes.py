#!/bin/python3

import os
import sys

#
# Complete the swapNodes function below.
#
class Node: 
    def __init__(self,key,depth): 
        self.left = None
        self.right = None
        self.val = key
        self.depth = depth 

    def addChildren(self,c):
        children = []
        if c[0] != -1:
            self.left = Node(c[0],self.depth+1)
            children.append(self.left)
        if c[1] != -1:
            self.right = Node(c[1],self.depth+1)
            children.append(self.right)
        return children

    def swap(self,d):
        if d == 1:
            if self.left is not None or self.right is not None:
                temp = self.left
                self.left = self.right
                self.right = temp
                del temp
        else:
            if self.left is not None:
                self.left.swap(d-1)
            if self.right is not None:
                self.right.swap(d-1)

    def inOrder(self,order=None):
        if order is None:
            order = []
        if self.left is not None:
            order = self.left.inOrder(order)

        order.append(self.val)

        if self.right is not None:
            order = self.right.inOrder(order)

        return order

def swapNodes(indexes, queries):
    maxDepth = 1
    root = Node(1,1)
    children = root.addChildren(indexes[0])
    while len(children) != 0:
        temp = []
        for c in children:
            if c.depth > maxDepth:
                maxDepth = c.depth
            temp += c.addChildren(indexes[c.val-1])
        children = temp
    

    orders = []
    for q in queries:
        depth = q
        while depth < maxDepth:
            root.swap(depth)
            depth += q
        order = root.inOrder()
        orders.append(order)
    return orders
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
