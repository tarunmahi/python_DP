import random

def guess(a):
    guess_num=random.randint(1,a)
    num=0
    while num!=guess_num:
        num=int(input(f"guess the number between 1 to {a} "))
        if num<guess_num:
            print("sorry too low")
        elif num>guess_num:
            print("sorry too high")
    print("yay you are correct")
    
#y=int(input("enter the range "))
#guess(y)

def guessed(num):
    low=1
    high=num
    vari=''
    while vari!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        vari=input(f" is the number {guess} too low too high or correct ")
        if vari=='h':
            high=guess-1
        elif vari=='l':
            low=guess+1
    print(f"yayy the value {guess} is correct")    
    
guessed(25)