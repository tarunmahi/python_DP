arr1=[4,2,7,9,22,165,789,345,672,432,56,43,87,99,12354,65,78,990]

class sort:
    def __init__(self,arr):
        self.arr=arr
    def insertion_sort(self):
        arr=self.arr
        n=len(arr)
        for i in range(1,n):
            key=arr[i]
            j=i-1
            while j>=0 and key<arr[j]:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        return arr
    def bubble_sort(self):
        arr=self.arr
        n=len(arr)
        for i in range(n-1):
            for j in range(n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
    def selection_sort(self):
        pass
    def radix_sort(self):
        pass
    def merge_sort(self):
        pass
    def heap_sort(self):
        pass
    def quick_sort(self):
        pass
    
val=sort(arr1)
print(val.bubble_sort())    