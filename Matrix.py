#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY roads
#  2. INTEGER_ARRAY machines
#
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.machine = [False] * size
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
                self.machine[root_u] = self.machine[root_u] or self.machine[root_v]
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
                self.machine[root_v] = self.machine[root_u] or self.machine[root_v]
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
                self.machine[root_u] = self.machine[root_u] or self.machine[root_v]
    
    def set_machine(self, u):
        root_u = self.find(u)
        self.machine[root_u] = True
    
    def has_machine(self, u):
        return self.machine[self.find(u)]
    

def minTime(roads, machines):
    n = len(roads) + 1
    uf = UnionFind(n)
    
    # Mark all machine nodes in the union-find structure
    for machine in machines:
        uf.set_machine(machine)
    
    # Sort roads by weight in descending order
    roads.sort(key=lambda x: -x[2])
    
    total_time = 0
    for u, v, w in roads:
        if uf.has_machine(u) and uf.has_machine(v):
            total_time += w
        else:
            uf.union(u, v)
    
    return total_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = []

    for _ in range(k):
        machines_item = int(input().strip())
        machines.append(machines_item)

    result = minTime(roads, machines)

    fptr.write(str(result) + '\n')

    fptr.close()
