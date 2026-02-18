# setters and getter for the class and attributes

'''
    Getters and setters are methods that let you control how the attributes of a class are accessed and modified.
    With getters you retrieve a value, and with setters you set a value.
        Getters let you retrieve a value or even compute a value on the fly.
        Setters let you modify the values safely by running checks before assignment.
        Properties are what tie these getters and setters together so you can write logic while still using dot notation.
        Deleters let you define what happens when an attribute is deleted.
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Getter
    @property
    def radius(self):
        return self._radius

    # Setter
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    # Deleter
    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius

# Create circle object with a radius
my_circle = Circle(33)
print("Initial radius:", my_circle.radius)  # 33

# Delete the radius
# This calls the deleter
del my_circle.radius # Deleting radius...
print("Radius deleted!") # Radius deleted!

# Try to access radius after deletion
try:
    print(my_circle.radius)
except AttributeError as e:
    print("Error:", e) # Error: 'Circle' object has no attribute '_radius'
