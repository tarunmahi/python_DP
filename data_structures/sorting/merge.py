class merge:
    def __init__(self,arr):
        self.arr=arr
    def mergesort(self,arr):
        if len(arr)<=1:
            return arr
        middle=len(arr)//2
        left=arr[:middle]
        right=arr[middle:]
        left=self.mergesort(left)
        right=self.mergesort(right)
        
        return self.merge(left,right)
    
    def merge(self,left,right):
        result=[]
        left_ind,right_ind=0,0
        while left_ind<len(left) and right_ind<len(right):
            if left[left_ind]<right[right_ind]:
                result.append(left[left_ind])
                left_ind+=1
            else:
                result.append(right[right_ind])
                right_ind+=1
        result.extend(left[left_ind:])
        result.extend(right[right_ind:])
        return result
arr1=[4,2,7,9,22,165,789,345,672,432,56,43,87,99,12354,65,78,990]
val=merge(arr1)
print(val.mergesort(arr1))