"""
Inheritance: Inheritance is a mechanism that allows a class (called a child class or derived class) 
to inherit properties and behaviors from another class (called a parent class or base class).
The child class can extend or modify the functionality of the parent class while reusing its existing code.
"""

class Animal:
    def __init__(self,animal):
        self.animal=animal
    def speak(self):
        raise Exception("it must be implemented from child")
class dog(Animal):
    def speak(self):
        print("wooffff")
class cat(Animal):
    def speak(self):
        print("meoww")
        
Dog=dog("buddy")
Cat=cat("whiskers")

Dog.speak()
Cat.speak()

class values:
    def __init__(self,name):
        self.name=name
        self.val=2345
        self.hero="tarun"

class vars(values):
    def speak(self):
        print(f"his name is given by mr {self.name} and his balance is {self.val} given by {self.hero} as status")
        
        
boss=vars("dhoni")
boss.speak()