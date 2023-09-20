#!/usr/bin/python3

"""A class Rectangle that inherits from Base"""
from models.base import Base

class Rectangle(Base):
    """A class rectnagle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The class constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """It retreives the width and ssign it to the right value"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """it sets the width and assign it to the right value"""
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """It retreives the height and assign it to the right value"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """It sets the height and ssign it to the right vlaue"""
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """It retreives the value of x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """It sets the value of x"""
        if (type(value) != int):
           raise TypeError("x must be an integer")
        if (value < 0):
           raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """It retrieves the value of y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """it sets the value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """It returns the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """It shows the stdout"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """It orints the statement"""
        value = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.__x,
                                                        self.__y,
                                                        self.__width,
                                                        self.__height)
        return (value)

    def update(self, *args, **kwargs):
        """It updates the args"""
        if (args and len(args) != 0):
            r = 0
            for a in args:
                if (r == 0):
                    if (a is None):
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = a
                elif (r == 1):
                    self.width = a
                elif (r == 2):
                    self.height = a
                elif (r == 3):
                    self.x = a
                elif (r == 4):
                    self.y = a
                r = r + 1
        elif kwargs and len(kwargs) != 0:
            for w, g in kwargs.items():
                if (w == "id"):
                    if (g is None):
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = g
                elif (w == "width"):
                    self.width = g
                elif (w == "height"):
                    self.height = v
                elif (w == "x"):
                    self.x = g
                elif (w == "y"):
                    self.y = g

    def to_dictionary(self):
        """It returs the json in the dictionary form"""
        return {'id': self.id,
                 'width': self.width,
                 'height': self.height,
                 'x': self.x,
                 'y': self.y}
