"""
Docstring for oop.polymorphism-notes
- This file contains notes and examples related to the concept of polymorphism in object-oriented programming (OOP).
- Polymorphism allows objects of different classes to be treated as objects of a common superclass.
- It enables a single interface to represent different underlying forms (data types).
- Polymorphism is often achieved through method overriding, where a child class provides a specific implementation
    of a method that is already defined in its parent class.
"""

class Animal:
   def speak(self):
       return 'Some generic sound'

class Cat(Animal):
   def speak(self):
       return 'A cat meow'

class Dog(Animal):
   def speak(self):
       return 'A dog barks woof woof'

class Monkey(Animal):
   def speak(self):
       return 'A monkey ooh ooh aah aah ooh ooh aah aah'
  
print(Cat().speak()) # A cat meow
print(Dog().speak()) # A dog barks woof woof
print(Monkey().speak()) # A monkey ooh ooh aah aah ooh ooh aah aah
print(Animal().speak()) # Some generic sound


animals = [Cat(), Dog(), Monkey()]

for animal in animals:
   print(animal.speak())

# Output:
# A cat meow
# A dog barks woof woof
# A monkey ooh ooh aah aah ooh ooh aah aah

### What is Name Mangling and How Does it Work?
# Name mangling is a mechanism in Python that allows for the creation of private attributes in classes.
# When an attribute name starts with two underscores (__) and does not end with two underscores,
# Python automatically changes the name of the attribute to include the class name, making it harder to access from outside the class.
# This is done to prevent accidental access and modification of private attributes from outside the class.

"""
    To remind you of the difference between them, a single underscore is a convention that means the attribute is 
    meant for internal use in the class and should not be directly accessed from outside the class. 
    Double underscore, on the other hand, prevents that attribute from being accessed directly from outside the class.
"""
class Example:
    def __init__(self):
        self._internal = 'I can be accessed from outside the class, but should not'
        self.__private = 'You cannot access me directly from outside the class'

obj = Example()

print(obj._internal) # I can be accessed from outside the class, but should not
# print(obj.__private)  # AttributeError: 'Example' object has no attribute '__private'

""""
    So, which should you use to prefix attributes between single underscore (_) and double underscore (__)? 
    It depends. If an attribute is only meant for internal use within the class, stick with a single underscore.
"""