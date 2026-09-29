# Practical 8
# Implementation of Graph and Searching (DFS and BFS)

from collections import deque


# Graph using adjacency list
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    # Add an edge
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)   # Remove this line for directed graph

    # DFS
    def dfs(self, start):
        visited = [False] * self.vertices
        result = []

        def dfs_recursive(vertex):
            visited[vertex] = True
            result.append(vertex)

            for neighbour in self.graph[vertex]:
                if not visited[neighbour]:
                    dfs_recursive(neighbour)

        dfs_recursive(start)
        return result

    # BFS
    def bfs(self, start):
        visited = [False] * self.vertices
        queue = deque()
        result = []

        visited[start] = True
        queue.append(start)

        while queue:
            vertex = queue.popleft()
            result.append(vertex)

            for neighbour in self.graph[vertex]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)

        return result


# Main program
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

g = Graph(n)

print("Enter edges (u v):")
for i in range(e):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start = int(input("Enter starting vertex: "))

print("DFS Traversal:", g.dfs(start))
print("BFS Traversal:", g.bfs(start))