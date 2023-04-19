

sentence = "the quick brown fox jumps over the lazy dog"

words=sentence.split(" ")
length=[len(x) for x in words if x!="the"]
print(length)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [float(num) for num in numbers if num%2==0]
print(newlist)