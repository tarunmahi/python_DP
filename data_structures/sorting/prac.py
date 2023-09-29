
class quicksort:
    def quicksort(self,arr,low,high):
        if low<high:
            pivotindex=self.partition(arr,low,high)
            self.quicksort(arr,low,pivotindex-1)
            self.quicksort(arr,pivotindex+1,high)
        return arr
    def partition(self,arr,low,high):
        pivot=arr[low]
        left=low+1
        right=high
        
        done=False
        while not done:
            while left<=right and arr[left]<=pivot:
                left+=1
            while right>=left and arr[right]>=pivot:
                right-=1
            if right<left:
                done=True
            else:
                arr[left],arr[right]=arr[right],arr[left]
        arr[right],arr[low]=arr[low],arr[right]
        return right
        
        
        
        
        
arr1=[4,2,7,9,22,165,789,345,672,432,56,43,87,99,12354,65,78,990]
val=quicksort()
print(val.quicksort(arr1,0,len(arr1)-1))
"""
def quick_sort_inplace(arr, low, high):
    if low < high:
        # Partition the array into two parts
        pivot_index = partition(arr, low, high)

        # Recursively sort the subarrays
        quick_sort_inplace(arr, low, pivot_index-1)
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
"""