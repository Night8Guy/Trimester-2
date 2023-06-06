#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize Rectangle class update meh """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Return width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Return height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Return x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Return y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Return area """
        return self.__width * self.__height

    def display(self):
        """ Print rectangles to stdout """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        me = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(me, x, y, w, h))

    def update(self, *args, **kwargs):
        """ Update attributes """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Return dictionary representation of Rectangle """
        me = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return {'id': me, 'width': w, 'height': h, 'x': x, 'y': y}
