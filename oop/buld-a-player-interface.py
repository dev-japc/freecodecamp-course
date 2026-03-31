import math

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"
        
    def set_width(self, width):
        self._width = width
    
    def set_height(self, height):
        self._height = height

    def get_area(self):
        return self._width * self._height

    def get_perimeter(self):
        return 2*(self._width + self._height)

    def get_diagonal(self):
        return math.sqrt(((self._width)**2) + ((self._height)**2))

    def get_picture(self):
        if self._width > 50 or self._height > 50:
            return 'Too big for picture.'

        asteriscs = ('*' * self._width) + '\n'
        return f"{asteriscs * (self._height)}"
    
    def get_amount_inside(self, shape):
        return (self._height // shape._height) * (self._width // shape._width)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self._side = side
        
    def __str__(self):
        return f"Square(side={self._side})"
    
    def set_width(self, side):
        super().set_height(side)
        super().set_width(side)
        self._side = side
    
    def set_height(self, side):
        super().set_height(side)
        super().set_width(side)
        self._side = side

    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)
        self._side = side
    


rect = Rectangle(10, 5)
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(5)
print(sq.get_area())
sq.set_side(4)
sq.set_height(3)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

print(rect.get_amount_inside(sq))