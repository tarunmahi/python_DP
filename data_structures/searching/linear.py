def linear_search(arr,key):
    for i in range(1,len(arr)+1):
        if arr[i]==key:
            return i
    return -1


arr1 = [2, 5, 7, 10, 15, 20 ,13]
arr=sorted(arr1)
target = 13
result = linear_search(arr, target)
if result != -1:
    print("Element", target, "found at index", result+1)
else:
    print("Element", target, "not found in the array.")