def kadanes(seq):
    curr_sum=0
    max__sum=0
    
    for i in range(0,len(seq)):
        curr_sum=max(seq[i],curr_sum+seq[i])
        max__sum=max(max__sum,curr_sum)
    return max__sum


arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f" the contigous or max sub array of values {arr} is {kadanes(arr)}")