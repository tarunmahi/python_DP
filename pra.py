class Binary:
    def __init__(self,seq):
        self.seq=seq
    def search(self,target):
        arr1=self.seq
        arr2=sorted(arr1)
        length=len(arr2)
        print(arr2)
        left=0
        right=length-1
        while left<=right:
            mid=(left+right)//2
            if arr2[mid]==target:
                return mid
            elif arr2[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1

arr1=[2,5,1,89,45,31,23,76]
ll=Binary(arr1)
result=ll.search(5)

if result==-1:
    print("element is not found in the series")
else:
    print(f"element is found at the index value of {result+1}")