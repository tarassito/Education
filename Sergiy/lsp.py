#Принцип LSP - клас спадок повинен доповнювати, а не заміщати поведінку базового класу.

class Rectangle():
    def __init__(self):
        self.width = 0
        self.height = 0

    def setHeight(self, value):
        self.height = value

    def setWidth(self, value):
        self.width = value

    def getSquare(self):
        print('Square is ', self.height * self.width)
        return self.height * self.width

    def getSides(self):
        print(f"Width is {self.width} Height is {self.height}")
        return (self.width, self.width)


a = Rectangle()
# set sides
a.setWidth(10)
a.getSides() # Width is 10 Height is 0

a.setHeight(20)
a.getSides() # Width is 10 Height is 20

a.getSquare() # Square is 200

#Change width
a.setWidth(30)
a.getSides() # Width is 30 Height is 20
a.getSquare() # Square is 600


class Square(Rectangle):
    def setHeight(self, value):
        self.height = value
        self.width = value

    def setWidth(self, value):
        self.width = value
        self.height = value

b = Square()
#set sides
b.setWidth(10)
b.getSides() # Width is 10 Height is 10

b.setHeight(20)
b.getSides() # Width is 20 Height is 20

b.getSquare() # Square is 400

#Change width
b.setWidth(30)
b.getSides() # Width is 30 Height is 30
b.getSquare() # Square is 900

#For example we have some validation for class Rectangle. We can try it with new class Square
def squareValidation(v_class):
    v_instance = v_class()
    v_instance.setWidth(10)
    v_instance.setHeight(20)

    return v_instance.getSquare() == 200

print(squareValidation(Rectangle)) #True
print(squareValidation(Square)) #False

#One of the solutions is to create abstract class Quadrangle and 2 subclasses: Square and Rectangle
from abc import *
class Quadrangle(metaclass = ABCMeta):

    def __init__(self):
        self.width = 0
        self.height = 0

    @abstractmethod
    def setHeight(self, value):
        self.height = value

    @abstractmethod
    def setWidth(self, value):
        self.width = value

    def getSquare(self):
        print('Square is ', self.height * self.width)

class Square(Quadrangle):
    def setHeight(self, value):
        self.height = value
        self.width = value

    def setWidth(self, value):
        self.width = value
        self.height = value

class Rectangle(Quadrangle):
    def setHeight(self, value):
        self.height = value

    def setWidth(self, value):
        self.width = value
