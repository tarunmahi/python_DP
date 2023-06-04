def kadanes(seq):
    curr_sum=0
    max_sum=0
    
    for i in range(len(seq)):
        curr_sum=max(seq[i],curr_sum+seq[i])
        max_sum=max(curr_sum,max_sum)
    return max_sum
    




arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f" the contigous or max sub array of values {arr} is {kadanes(arr)}")