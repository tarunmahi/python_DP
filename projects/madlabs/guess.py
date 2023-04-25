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
    
y=int(input("enter the range "))
#guess(y)

def computer():
    
