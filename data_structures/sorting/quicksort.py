def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort the two sub-arrays
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # Choose the rightmost element as the pivot
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        # If the current element is less than or equal to the pivot, swap it with the element at index i
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot element at its correct position in the sorted array
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quick_sort(array, 0, len(array) - 1)
print(array)
