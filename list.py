

sentence = "the quick brown fox jumps over the lazy dog"

words=sentence.split(" ")
length=[len(x) for x in words if x!="the"]
print(length)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [float(num) for num in numbers if num%2==0]
print(newlist)

#lambda functions

l = [2,4,7,3,14,19]

for num in l:
    check=lambda num:(num%2)==1
    print(check(num))
    
#lambda function 
## function name = lambda inputs:outputs

#map functions
## map(func , *iterables)
ll = [2,4,7,3,14,19]

lll=list(map(ll*10,ll))
print(lll)