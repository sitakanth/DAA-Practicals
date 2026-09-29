# Practical 9
# Implementation of Prim's Algorithm

INF = 999999


def prim(graph, vertices):
    selected = [False] * vertices
    selected[0] = True

    total_cost = 0

    print("\nEdges in Minimum Spanning Tree:")

    for _ in range(vertices - 1):
        minimum = INF
        x = 0
        y = 0

        for i in range(vertices):
            if selected[i]:
                for j in range(vertices):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(f"{x} -- {y} = {minimum}")

        total_cost += minimum
        selected[y] = True

    print("Total cost of MST:", total_cost)


# Main program
n = int(input("Enter number of vertices: "))

graph = [[0] * n for _ in range(n)]

print("Enter weighted edges.")
print("Enter 0 if there is no edge.")

for i in range(n):
    for j in range(i + 1, n):
        weight = int(input(f"Weight between {i} and {j}: "))
        graph[i][j] = weight
        graph[j][i] = weight

prim(graph, n)