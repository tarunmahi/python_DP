"""
Polymorphism: Polymorphism refers to the ability of objects of different classes to respond to the same method or attribute in different ways. 
It allows different objects to be treated uniformly based on their common characteristics or interfaces.
"""
class Dog:
    def sound(self):
        print("bark")
class cat:
    def sound(self):
        print("meow")
class cow:
    def sound(self):
        print("moooohhhh")
        
a=Dog()
b=cat()
c=cow()
a.sound()
b.sound()
c.sound()