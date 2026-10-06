# Practical 12
# Travelling Salesman Problem

from itertools import permutations

n = int(input("Enter number of cities: "))

print("Enter the cost matrix:")
cost = []

for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

# Start from city 0
cities = list(range(1, n))

min_cost = float('inf')
best_path = None

# Generate all possible routes
for path in permutations(cities):
    current_path = [0] + list(path) + [0]

    total_cost = 0

    for i in range(len(current_path) - 1):
        total_cost += cost[current_path[i]][current_path[i + 1]]

    if total_cost < min_cost:
        min_cost = total_cost
        best_path = current_path

print("\nMinimum Cost =", min_cost)

print("Best Route:", end=" ")
for city in best_path:
    print(city, end=" ")