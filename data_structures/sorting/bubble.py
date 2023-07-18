"""_summary_
time complexity:- o(n^2)
space complexity:- o(1)
"""

def bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    return arr



arr1=[5,4,3,1,2,7,6,56]

print(bubblesort(arr1))
    