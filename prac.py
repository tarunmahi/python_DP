
"""class Heap:
    def heapify(self,seq,n,i):
        largest=i
        left=2*i+1
        right=2*i+2
        if left<n and seq[left]>seq[largest]:
            largest=left
        if right<n and seq[right]>seq[largest]:
            largest=right
        if largest!=i:
            seq[i],seq[largest]=seq[largest],seq[i]
            self.heapify(seq,n,largest)
    def heap_sort(self,seq):
        n=len(seq)
        
        for i in range((n//2)-1,-1,-1):
            self.heapify(seq,n,i)
        for i in range(n-1,0,-1):
            seq[0],seq[i]=seq[i],seq[0]
            self.heapify(seq,i,0)
        return seq 

"""
class Heap:
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







arr1=[5,4,3,1,2,7,6,56]
val=Heap()
print(val.heap_sort(arr1))