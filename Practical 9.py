# Practical 9: Prim's Algorithm

INF = 999999

# Weighted adjacency matrix
graph = [
    [0, 2, INF, 6, INF],
    [2, 0, 3, 8, 5],
    [INF, 3, 0, INF, 7],
    [6, 8, INF, 0, 9],
    [INF, 5, 7, 9, 0]
]

n = len(graph)

selected = [False] * n
selected[0] = True

total_cost = 0

print("Edges in Minimum Spanning Tree:")

for _ in range(n - 1):

    minimum = INF
    x = 0
    y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] < minimum:
                    minimum = graph[i][j]
                    x = i
                    y = j

    print(x, "--", y, ":", minimum)

    total_cost += minimum
    selected[y] = True

print("Minimum Cost =", total_cost)