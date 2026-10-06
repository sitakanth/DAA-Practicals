# Practical 11
# Implement Floyd-Warshall Algorithm

INF = 99999

n = int(input("Enter number of vertices: "))

print("Enter the adjacency matrix:")
print("Enter", INF, "for no direct edge.")

graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# Floyd-Warshall Algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(
                graph[i][j],
                graph[i][k] + graph[k][j]
            )

print("\nShortest Distance Matrix:")

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print("INF", end="\t")
        else:
            print(graph[i][j], end="\t")
    print()