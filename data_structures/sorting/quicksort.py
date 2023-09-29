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

def quick_sort_inplace(arr, low, high):
    if low < high:
        # Partition the array into two parts
        pivot_index = partition(arr, low, high)

        # Recursively sort the subarrays
        quick_sort_inplace(arr, low, pivot_index)
        quick_sort_inplace(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # Swap arr[left] and arr[right]
            arr[left], arr[right] = arr[right], arr[left]

    # Swap arr[low] and arr[right]
    arr[low], arr[right] = arr[right], arr[low]

    return right

# Example usage:
if __name__ == "__main__":
    unsorted_array = [3, 6, 8, 10, 1, 2, 1]
    quick_sort_inplace(unsorted_array, 0, len(unsorted_array) - 1)
    print(unsorted_array)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
if __name__ == "__main__":
    unsorted_array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quick_sort(unsorted_array)
    print(sorted_array)
