"""
Classes: A class is a blueprint or template for creating objects. It defines the properties (attributes) 
and behaviors (methods) that objects of the class should have. Classes are defined using the class keyword.

Objects: An object is an instance of a class. It represents a specific entity with its own unique set of 
properties and behaviors. Objects are created from a class using the class name followed by parentheses.
"""

class car:
    def __init__(self,comp,type):
        self.comp=comp
        self.type=type
    def drive(self):
        print(f" tarun is drivin {self.comp} car with model {self.type}")
        
        
        
car1=car("pagani","sports")
car2=car("tesla","EV")
car3=car("honda","SUV")

car1.drive()
car2.drive()
car3.drive()