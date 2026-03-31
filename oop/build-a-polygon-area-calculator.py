class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def set_width(self, width):
        pass

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def set_width(self, width):
        self._width = width
        self._height = width
    def set_height(self, height):
        self._width = height
        self._height = height
    def __str__(self):
        return super().__str__()