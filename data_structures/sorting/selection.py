"""
space complexity:- o(n^2)
time complexity:- o(1)
"""
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[min_index],arr[i]=arr[i],arr[min_index]
    return arr

arr1=[5,4,3,1,2,7,6,56]

print(selection_sort(arr1))

