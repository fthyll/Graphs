#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n * c_lib
    
    # Construct the graph
    graph = {i: [] for i in range(1, n+1)}
    for city in cities:
        u, v = city
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(node, visited):
        visited.add(node)
        count = 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                count += dfs(neighbor, visited)
        return count
    
    total_cost = 0
    visited = set()
    for i in range(1, n+1):
        if i not in visited:
            connected_cities = dfs(i, visited)
            total_cost += c_lib + (connected_cities - 1) * c_road
    
    return total_cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
