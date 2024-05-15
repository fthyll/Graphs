class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]
    
    def connect(self, x, y):
        self.edges[x].append(y)
        self.edges[y].append(x)
    
    def find_all_distances(self, start):
        distances = [-1] * self.n
        queue = deque([start])
        distances[start] = 0
        
        while queue:
            current = queue.popleft()
            current_distance = distances[current]
            
            for neighbor in self.edges[current]:
                if distances[neighbor] == -1:  # If not visited
                    distances[neighbor] = current_distance + 6
                    queue.append(neighbor)
        
        # Exclude the start node's distance from the output
        output = [distances[i] for i in range(self.n) if i != start]
        print(" ".join(map(str, output)))

if __name__ == "__main__":
    from collections import deque
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        graph = Graph(n)
        for _ in range(m):
            x = int(data[index])
            y = int(data[index + 1])
            index += 2
            graph.connect(x - 1, y - 1)
        
        s = int(data[index])
        index += 1
        graph.find_all_distances(s - 1)
