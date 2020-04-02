#!/bin/python3

import os
import sys

class Node:
    def __init__(self, ID, edges=None):
        self.ID = ID
        if edges is None:
            self.edges = []
        else:
            self.edges = edges
        
    def add_edge(self, edge):
        self.edges.append(edge)

class Tree:
    def __init__(self, n, r):
        self.n = n
        self.r = r
        self.nodes = [None]
        for i in range(1,n+1):
            self.nodes.append(Node(i))
    
    def add_edges(self, edges):
        for e in edges:
            (self.nodes[e[0]]).add_edge(e[1])
            (self.nodes[e[1]]).add_edge(e[0])
    
    def num_subtrees(self):
        num = 0
        dist_depth = set()
        dist_level_size = [set() for _ in range(r)]
        dist_level_parents = [set() for _ in range(r)]
        dist_level_parents[0].add(1)
        for i in range(1,self.n+1):
            new = False
            num_edges = 0
            first_level = (self.nodes[i]).edges
            subtree = [[(i,f) for f in first_level]]
            sub_count = [[len(first_level)]]
            if len(first_level) not in dist_level_size[0]:
                new = True
                dist_level_size[0].add(len(first_level))
            num_edges += len(first_level)
            depth = r
            for d in range(r-1):
                next_level = []
                next_count = []
                for s in subtree[-1]:
                    sub_next = [(s[1],x) for x in (self.nodes[s[1]]).edges if x!=s[0]]
                    if len(sub_next) != 0:
                        next_level += sub_next
                        next_count.append(len(sub_next))
                num_edges += len(next_level)
                if len(next_level) == 0:
                    depth = d + 1
                    continue
                sub_count.append(next_count)
                subtree.append(next_level)
                if len(next_level) not in dist_level_size[d+1]:
                    new = True
                    dist_level_size[d+1].add(len(next_level))
                if len(next_count) not in dist_level_parents[d+1]:
                    new = True
                    dist_level_parents[d+1].add(len(next_count))
                
            if depth not in dist_depth:
                new = True
                dist_depth.add(depth)
            # check if repeated subtree
            if new:
                num += 1
            # print(i,num_edges, subtree)
        return num

def jennysSubtrees(n, r, edges):
    tree = Tree(n, r)
    tree.add_edges(edges)
    return tree.num_subtrees()
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().split()

    n = int(nr[0])

    r = int(nr[1])

    edges = []

    for _ in range(n-1):
        edges.append(list(map(int, input().rstrip().split())))

    result = jennysSubtrees(n, r, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
