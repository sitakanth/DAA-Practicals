# Practical 6: Matrix Chain Multiplication
# Using Dynamic Programming

def matrix_chain_order(p):
    n = len(p) - 1

    # dp[i][j] stores minimum multiplication cost
    dp = [[0 for _ in range(n + 1)]
          for _ in range(n + 1)]

    # Chain length
    for length in range(2, n + 1):

        for i in range(1, n - length + 2):

            j = i + length - 1

            dp[i][j] = float('inf')

            for k in range(i, j):

                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n]


# Input
n = int(input("Enter number of matrices: "))

print("Enter dimensions of matrices.")

print("For n matrices, enter n+1 dimensions.")

p = list(map(int, input("Enter dimensions: ").split()))

# Calculate minimum multiplication cost
result = matrix_chain_order(p)

print("Minimum number of scalar multiplications:", result)

Sample Input:-

Suppose we have:

A1 = 10 × 20
A2 = 20 × 30
A3 = 30 × 40

Input:

Enter number of matrices: 3
Enter dimensions: 10 20 30 40


Sample Output:-
Minimum number of scalar multiplications: 18000

Complexity:-

For n matrices:

Time Complexity  = O(n³)
Space Complexity = O(n²)