"""
time complexity:- o(n^2)
space complexity:- o(1) inplace sorting algorithmn
"""
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr1=[5,4,3,1,2,7,6,56]

print(insertion_sort(arr1))

