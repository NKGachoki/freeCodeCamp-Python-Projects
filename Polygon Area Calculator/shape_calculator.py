class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    # Method to return object shape
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = []
            for i in range(self.height):
                picture.append(f"{''.join(['* ' for j in range(self.width) if j != None])}\n")
            picture = (''.join(picture))
            return picture
    
    # Method to return the no. of times a polygon of Rectangle class or other Child class can fit in object
    def get_amount_inside(self, shape):
        amount_inside = self.get_area()/shape.get_area()
        amount_inside = round(amount_inside)
        return amount_inside
    
    def __repr__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"
    
class Square(Rectangle):
    
    def __init__(self, side):
        self.side = side
        self.width = self.side
        self.height = self.side

    def set_side(self, new_side):
        self.side = new_side
        self.width = new_side
        self.height = new_side

    def set_height(self, new_height):
        self.height = new_height
        self.width = new_height

    def set_width(self, new_width):
        self.height = new_width
        self.width = new_width

    def __repr__(self):
        return f"{self.__class__.__name__}(side={self.side})"