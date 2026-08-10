# Practical 5: 0/1 Knapsack using Dynamic Programming

def knapsack(weights, values, capacity):
    n = len(values)

    # DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Build table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Input
n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))

capacity = int(input("Enter knapsack capacity: "))

# Calculate maximum value
result = knapsack(weights, values, capacity)

print("Maximum Profit:", result)

Sample Input:- 
Enter number of items: 4
Enter weights: 2 3 4 5
Enter values: 3 4 5 6
Enter knapsack capacity: 5


Sample Output:-
Maximum Profit: 7


Complexity:-

For n items and capacity W:

Time Complexity  = O(nW)
Space Complexity = O(nW)

