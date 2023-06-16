def heapify(arr,n,i):
    largest=i
    left=i*2+1
    right=i*2+2
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
        
def heap_sort(seq):
    n=len(seq)
    for i in range((n//2)-1,-1,-1):
        heapify(seq,n,i)
    for i in range(n-1,0,-1):
        seq[0],seq[i]=seq[i],seq[0]
        heapify(seq,i,0)
    return seq




array = [9, 5, 2, 8, 1, 10]
sorted_array = heap_sort(array)
print(sorted_array)
