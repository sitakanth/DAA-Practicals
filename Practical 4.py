# Practical 4: Factorial using Iterative and Recursive Methods

def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)


# Input
n = int(input("Enter a positive integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("\nFactorial using Iterative Method:",
          factorial_iterative(n))

    print("Factorial using Recursive Method:",
          factorial_recursive(n))

Sample Input:-
Enter a positive integer: 5


Sample Output:-
Factorial using Iterative Method: 120
Factorial using Recursive Method: 120


Complexity:-
Iterative
Time Complexity = O(n)
Space Complexity = O(1)
Recursive
Time Complexity = O(n)
Space Complexity = O(n)