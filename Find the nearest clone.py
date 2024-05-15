#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
from collections import deque, defaultdict

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # Build the adjacency list for the graph
    graph = defaultdict(list)
    for u, v in zip(graph_from, graph_to):
        graph[u].append(v)
        graph[v].append(u)
    
    # Find all nodes with the target color
    target_nodes = [i+1 for i, color in enumerate(ids) if color == val]
    
    # If there are less than 2 nodes with the target color, return -1
    if len(target_nodes) < 2:
        return -1
    
    # Function to perform BFS from a given start node
    def bfs(start_node):
        visited = [-1] * (graph_nodes + 1)
        queue = deque([(start_node, 0)])
        visited[start_node] = 0
        while queue:
            current_node, current_distance = queue.popleft()
            for neighbor in graph[current_node]:
                if visited[neighbor] == -1:  # not visited
                    visited[neighbor] = current_distance + 1
                    queue.append((neighbor, current_distance + 1))
                    # If we find another target node, return the distance
                    if ids[neighbor - 1] == val:
                        return visited[neighbor]
        return float('inf')
    
    # Try BFS from each target node and find the minimum distance
    shortest_path = float('inf')
    for node in target_nodes:
        shortest_path = min(shortest_path, bfs(node))
    
    return shortest_path if shortest_path != float('inf') else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
