def binary_search(arr,val):
    left=0
    right=len(arr)-1
    
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==val:
            return mid
        if arr[mid]>val:
            right=mid-1
        else:
            left=mid+1
    return -1

arr = [2, 5, 7, 10, 15, 20]
target = 10
result = binary_search(arr, target)
if result != -1:
    print("Element", target, "found at index", result)
else:
    print("Element", target, "not found in the array.")