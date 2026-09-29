# Practical 10
# Implementation of Kruskal's Algorithm


# Find the parent of a vertex
def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]


# Union of two sets
def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

        return True

    return False


def kruskal(vertices, edges):
    # Sort edges according to weight
    edges.sort(key=lambda x: x[2])

    parent = []
    rank = []

    for i in range(vertices):
        parent.append(i)
        rank.append(0)

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if union(parent, rank, u, v):
            mst.append((u, v, weight))
            total_cost += weight

            # MST contains V-1 edges
            if len(mst) == vertices - 1:
                break

    print("\nEdges in Minimum Spanning Tree:")

    for u, v, weight in mst:
        print(f"{u} -- {v} = {weight}")

    print("Total cost of MST:", total_cost)


# Main program
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges in the format: source destination weight")

for i in range(e):
    u, v, weight = map(int, input().split())
    edges.append((u, v, weight))

kruskal(n, edges)