# Practical 2: Linear Search and Binary Search

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Input
arr = list(map(int, input("Enter elements separated by space: ").split()))
key = int(input("Enter element to search: "))

# Linear Search
linear_result = linear_search(arr, key)

if linear_result != -1:
    print("Linear Search: Element found at index", linear_result)
else:
    print("Linear Search: Element not found")


# Binary Search requires sorted array
arr.sort()
print("Sorted Array:", arr)

binary_result = binary_search(arr, key)

if binary_result != -1:
    print("Binary Search: Element found at index", binary_result)
else:
    print("Binary Search: Element not found")


Sample Input :- 
Enter elements separated by space: 45 12 78 34 23 90
Enter element to search: 34


Sample Output :-
Linear Search: Element found at index 3
Sorted Array: [12, 23, 34, 45, 78, 90]
Binary Search: Element found at index 2


Complexity :-
Algorithm	Best	Average	Worst	Space
Linear Search	O(1)	O(n)	O(n)	O(1)
Binary Search	O(1)	O(log n)	O(log n)	O(1)