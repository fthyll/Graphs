#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxRegion' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def maxRegion(grid):
    # Dimensions of the grid
    n = len(grid)
    m = len(grid[0])
    
    # Helper function to perform DFS
    def dfs(x, y):
        # Stack for DFS
        stack = [(x, y)]
        region_size = 0
        while stack:
            cx, cy = stack.pop()
            if 0 <= cx < n and 0 <= cy < m and grid[cx][cy] == 1:
                # Mark the cell as visited
                grid[cx][cy] = -1
                region_size += 1
                # Explore all 8 possible directions
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx != 0 or dy != 0:
                            stack.append((cx + dx, cy + dy))
        return region_size
    
    max_size = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                # Start a new DFS to calculate the region size
                size = dfs(i, j)
                max_size = max(max_size, size)
    
    return max_size

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    m = int(input().strip())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()

