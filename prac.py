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
    
"""

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

