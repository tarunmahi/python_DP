def quick_sort(arr,low,high):
    if low<high:
        partiton_index=partition(arr,low,high)
        
        quick_sort(arr,low,partiton_index-1)
        quick_sort(arr,partiton_index+1,high)
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if pivot>=arr[j]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quick_sort(array, 0, len(array) - 1)
print(array)