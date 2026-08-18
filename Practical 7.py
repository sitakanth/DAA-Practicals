# Practical 7
# Implementation of Making Change Problem using Dynamic Programming

def min_coins(coins, amount):
    # dp[i] stores the minimum number of coins required
    # to make amount i
    dp = [float('inf')] * (amount + 1)

    # Base case
    dp[0] = 0

    # Calculate minimum coins for each amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If amount cannot be formed
    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


# Main program
coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter the amount: "))

result = min_coins(coins, amount)

if result == -1:
    print("Change cannot be made for the given amount.")
else:
    print("Minimum number of coins required:", result)