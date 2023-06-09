""" Create class circle"""

class Circle:

    def __init__(self, circle_radius):
        """ initialize parameters """
        self.radius = circle_radius

    def area(self):
        """ calculate area of rectangle"""
        area = 3.14 * (self.radius ** 2)
        return area

    def peri(self):
        """ calculate perimeter of rectangle """
        peri = 2 * (3.14 * self.radius)
        return peri


""" create class square """

class Square:
    def __init__(self, square_side):
        self.side = square_side

    def area(self):
        """ area """
        area = self.side ** 2
        return area

    def peri(self):
        """ perimeter"""
        peri = 4 * self.side
        return peri


""" create class rectangle """

class Rectangle:
    def __init__(self, rectangle_length, rectangle_breadth):
        self.length = rectangle_length
        self.breadth = rectangle_breadth

    def area(self):
        """ area """
        area = self.length * self.breadth
        return area

    def peri(self):
        """ perimeter """
        peri = 2 * self.length + self.breadth
        return peri


""" create class triangle"""

class Triangle:
    def __init__(self, tri_side1, tri_side2, tri_side3, tri_height):
        self.side1 = tri_side1
        self.side2 = tri_side2
        self.side3 = tri_side3
        self.height = tri_height

    def area(self):
        """ area """
        area = 0.5 * self.side2 * self.height
        return area

    def peri(self):
        """ Perimeter """
        peri = self.side1 + self.side2 + self.side3
        return peri


cir = Circle(24.0)
sqr = Square(10)
rec = Rectangle(5, 7)
tri = Triangle(2, 3, 5, 10)

while True:
    ch = input("1.Circle\n2.Square\n3.Rectangle\n4.Triangle\n5.exit\n")
    if ch == '1':
        print("Area of circle are:", cir.area())
        print("Perimeter of circle are:", cir.peri())
    elif ch == "2":
        print("Area of Square are:%f", sqr.area())
        print("Perimeter of Square are:", sqr.peri())
    elif ch == "3":
        print("Area of Rectangle are:", rec.area())
        print("Perimeter of Rectangle are:", rec.peri())
    elif ch == "4":
        print("Area of Triangle are:", tri.area())
        print("Perimeter of Triangle are:", tri.peri())
    elif ch == "5":
        print("exit")
        break
