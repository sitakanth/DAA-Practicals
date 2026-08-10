# Practical 3: Max-Heap Sort

def heapify(arr, n, i):
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        heapify(arr, i, 0)

    return arr


# Input
arr = list(map(int, input("Enter elements separated by space: ").split()))

print("Original Array:", arr)

heap_sort(arr)

print("Sorted Array:", arr)

Sample Input :- 
Enter elements separated by space: 20 10 30 5 15 40


Sample Output:-
Original Array: [20, 10, 30, 5, 15, 40]
Sorted Array: [5, 10, 15, 20, 30, 40]


Complexity :-
Operation	Complexity
Build Max Heap	O(n)
Heapify	O(log n)
Heap Sort	O(n log n)
Best Case	O(n log n)
Average Case	O(n log n)
Worst Case	O(n log n)
Space	O(log n)