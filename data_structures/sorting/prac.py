def Merge_sort(A):
    if len(A)>1:
        
        mid=len(A)//2
        lefth=A[:mid]
        righth=A[mid:]
        Merge_sort(lefth)
        Merge_sort(righth)
        i=j=k=0
        while i<len(lefth) and j<len(righth):
            if lefth[i]<righth[i]:
                A[k]=lefth[i]
                i=i+1
            else:
                A[k]=righth[j]
                j=j+1
            k=k+1
        while i<len(lefth):
            A[k]=lefth[i]
            i=i+1
            k=k+1
        while j<len(righth):
            A[k]=righth[j]
            j=j+1
            k=k+1
        return A

arr=[9,8,7,6,5,4,3,2,1]
Merge_sort(arr)
print(arr)
        
        
            