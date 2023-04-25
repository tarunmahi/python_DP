#rock paper and scissors
import random
def play():
    choice=input("what is your choice 'r' or 'p ' or 's' ")
    computer=random.choice(['r','p','s'])
    if is_win(choice,computer):
        print("yay you had won")

    else:
        print("you lost")

def is_win(ch,com):
    if (ch=='r' and com=='s') or (ch=='s' and com=='p') or (ch=='p' and com=='r'):
        return True
    else:
        return False
play()