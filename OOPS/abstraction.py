"""
Abstraction: Abstraction is the process of representing complex real-world entities as simplified models within a program. 
It involves hiding the unnecessary details and exposing only the essential features and behaviors.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.make_sound())   # Output: Woof!
print(cat.make_sound())   # Output: Meow!