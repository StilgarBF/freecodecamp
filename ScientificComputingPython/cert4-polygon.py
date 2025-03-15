'''
In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class 
should be a subclass of Rectangle, and inherit its methods and attributes.

Rectangle class
When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain 
the following methods:

set_width
set_height
get_area: Returns area (width * height)
get_perimeter: Returns perimeter (2 * width + 2 * height)
get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
get_picture: Returns a string that represents the shape using lines of '*'. The number of lines should be equal to the height 
and the number of '*' in each line should be equal to the width. There should be a new line (\n) at the end of each line. If 
the width or height is larger than 50, this should return the string: 'Too big for picture.'.
get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape 
could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in 
two squares with sides of 4.
Additionally, if an instance of a Rectangle is represented as a string, it should look like: 'Rectangle(width=5, height=10)'.

Square class
The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The 
__init__ method should store the side length in both the width and height attributes from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a set_side method. If an 
instance of a Square is represented as a string, it should look like: 'Square(side=9)'.

Additionally, the set_width and set_height methods on the Square class should set both the width and height.
'''
class Rectangle:
    width: int
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        return "\n".join('*' *self.width for _ in range(self.height))+ "\n"

    def get_amount_inside(self, rect):
        return self.width // getattr(rect, 'width') * self.height // getattr(rect, 'height')

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)

s = Square(4)
print(f'Area:               {s.get_area()}')
print(f'Diagonal:           {s.get_diagonal()}')
print(f'Perimeter:          {s.get_perimeter()}')
print(f'Amount inside 2x1:  {s.get_amount_inside(Rectangle(2, 1))}')
print(f'Amount inside 3x3:  {s.get_amount_inside(Square(3))}')
print(f'Picture:\n{s.get_picture()}')
print("\n")
r = Rectangle(10, 5)
print(f'Rectangle:          {r}')
print(f'Area:               {r.get_area()}')
print(f'Amount inside 8x2:  {r.get_amount_inside(Rectangle(8, 2))}')
r.set_height(3)
print(f'Rectangle:          {r}')
print(f'Area:               {r.get_area()}')
print(f'Diagonal:           {r.get_diagonal()}')
print(f'Perimeter:          {r.get_perimeter()}')
print(f'Amount inside 8x2:  {r.get_amount_inside(Rectangle(8, 2))}')
print(f'Picture:\n{r.get_picture()}')
