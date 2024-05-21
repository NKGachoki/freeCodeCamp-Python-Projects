"""Module containing all classes and methods for polygon area calculator"""

class Rectangle:
    """Class representing rectangle objects"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        """Method to set width of rectangle object"""
        self.width = new_width

    def set_height(self, new_height):
        """Method to set height of rectangle object"""
        self.height = new_height

    def get_area(self):
        """Method to calculate area of rectangle object"""
        return self.width * self.height

    def get_perimeter(self):
        """Method to calculate perimeter of rectangle object"""
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        """Method to calculate diagonal of rectangle object"""
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        """Method to return object shape"""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = []
            for i in range(self.height):
                picture.append(f"{''.join(['*' for j in range(self.width) if j is not None])}\n")
            picture = ''.join(picture)
            return picture

    def get_amount_inside(self, shape):
        """Method to return the no. of times another polygon can fit in object"""
        amount_inside = self.get_area()/shape.get_area()
        amount_inside = round(amount_inside)
        return amount_inside

    def __repr__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"

class Square(Rectangle):
    """Child class of Rectangle""" 

    def __init__(self, side):
        self.side = side
        self.width = self.side
        self.height = self.side

    def set_side(self, new_side):
        """Method to set side of square object"""
        self.side = new_side
        self.width = new_side
        self.height = new_side

    def set_height(self, new_height):
        """Method to set height(and consequently width) of square object"""
        self.height = new_height
        self.width = new_height

    def set_width(self, new_width):
        """Method to set width(and consequently height) of square object"""
        self.height = new_width
        self.width = new_width

    def __repr__(self):
        return f"{self.__class__.__name__}(side={self.side})"
    