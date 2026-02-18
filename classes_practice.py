class Dog:
    species = 'Canis' #class attribute example
    def __init__(self, name): #special method created when an instance of the class is created
        self.name =  name #instance attribute example
    def bark(self):
        print(f'{self.name} woof')
my_dogo = Dog('Betto')
print(my_dogo.name) # Betto
print(my_dogo.species) # Canis

'''
    Attributes: are variables that belong to an object, so they hold data.
    there are instance attributes and class attributes.

    instance attributes: are those unique to each instance of a class, and we set them using
    the __init__ method.
    class attributes: belong to the class itself and are shared by all instances of that class.

    Note: you can access class attributes directly from the class itself, 
    but you need to create an object and pass it data first before you can access instance attributes.
'''
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model # Instance attributes
    
    def describe(self):
        return f'This car is a {self.color} {self.model}'
toyota_car = Car('gray', 'Toyota Yaris')
print(toyota_car.describe()) # This car is a gray Toyota Yaris

# for attr in dir(Car):
#     print(attr)

for attr in dir(toyota_car):
    # Ignore dunder methods like __init__ or __str__ and regular methods
    if not attr.startswith('__') and not callable(getattr(toyota_car, attr)):
        value = getattr(toyota_car, attr)
        print(f'{attr}: {value}')
'''
    hasattr(): checks if an object has a specific attribute.
    getattr(): retrieves the value of a specific attribute from an object.
    delattr(): deletes a specific attribute from an object.
    setattr(): sets or updates the value of a specific attribute on an object.
'''