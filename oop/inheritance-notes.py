"""
Docstring for inheritance-notes

- This file contains notes and examples related to the concept of inheritance in object-oriented programming (OOP).
- inheritance allows a child class (subclass) to inherit attributes and methods from a parent class (superclass)
- the child can have its own unique attributes and methods, in addition to those inherited from the parent class
- this promotes code reusability and helps to create a hierarchical relationship between classes

- child classes can override methods from the parent class to provide specific implementations
- child classes can also call methods from the parent class using the super() function
- child classes can have multiple levels of inheritance, where a child class can also be parent to another class

"""
class Walker:
    def walk(self):
        return 'I can walk on land'

class Swimmer:
    def swim(self):
        return 'I can swim in water'

# Amphibian inherits from both Walker and Swimmer
class Amphibian(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I'm {self.name} the frog. {self.walk()} and {self.swim()}."

frog = Amphibian('Freddy')
print(frog.introduce())
# Output: I'm Freddy the frog. I can walk on land and I can swim in water.