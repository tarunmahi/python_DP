arr="tarun"

l=[]
l2=[]
for i in range(len(arr)):
    l.append(arr[i])
for j  in range(len(l)):
    l2.append(l.pop())
print(l2)