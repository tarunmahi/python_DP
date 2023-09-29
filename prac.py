"""
def selection_sort(arr):
    n=len(arr)
    
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr


def bubble_sort(arr):
    n=len(arr)
    
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[5,4,3,1,2,7,6,5,34,12,98,65,38]

def insert_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

class heap:
    def heapify(self,arr,n,i):
        largest=i
        left=2*i+1
        right=2*i+2
        if left<n and arr[left]>arr[largest]:
            largest=left
        if right<n and arr[right]>arr[largest]:
            largest=right
        if largest!=i:
            arr[i],arr[largest]=arr[largest],arr[i]
            self.heapify(arr,n,largest)
    
    def heap_sort(self,arr):
        n=len(arr)
        for i in range((n//2)-1,-1,-1):
            self.heapify(arr,n,i)
        for i in range(n-1,0,-1):
            arr[0],arr[i]=arr[i],arr[0]
            self.heapify(arr,i,0)
        return arr
        
"""


"""
def bs(arr,low,high,val):
    mid=(low+high)//2
    if(arr[mid]==val):
        return mid;
    elif(arr[mid]>val):
        bs(arr,low,mid-1,val)
    elif(arr[mid]<val):
        bs(arr,mid+1,high,val)
    else:
        return 0
key=bs(arr,0,len(arr)-1,val)

if(key):
    print(f"element found at index {key}")
else:
    print("element  not found")
    


def insertion_sort(arr):
    n=len(arr)
    for i in range(n):
        key=arr[i]
        j=i-1
        
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr



arr=[5,4,3,1,2,7,6,5,34,12,98,25,65,38]
print(insertion_sort(arr))

"""
class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        left_ind, right_ind = 0, 0
        while left_ind < len(left) and right_ind < len(right):
            if left[left_ind] < right[right_ind]:
                result.append(left[left_ind])
                left_ind += 1
            else:
                result.append(right[right_ind])
                right_ind += 1
        result.extend(left[left_ind:])
        result.extend(right[right_ind:])
        return result

arr1 = [4, 2, 7, 9, 22, 165, 789, 345, 672, 432, 56, 43, 87, 99, 12354, 65, 78, 990]
ms = MergeSort(arr1)
sorted_arr = ms.merge_sort(arr1)
print(sorted_arr)
