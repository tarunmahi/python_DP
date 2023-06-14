def insertion_sort(seq):
    for i in range(1,len(seq)):
        key=seq[i]
        j=i-1
        while j>=0 and key<seq[j]:
            seq[j+1]=seq[j]
            j=j-1
        seq[j+1]=key
    return seq

arr1=[5,4,3,1,2,7,6,56]

print(insertion_sort(arr1))