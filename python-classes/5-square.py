#!/usr/bin/python3
"""Printing a square: """


class Square(object):
    """class variable size"""
    def __init__(self, size=0):
        """initialize size"""
        self.__size = size

    @property
    def size(self):
        """Property"""
        return self.__size

    @size.setter
    def size(self, value):
        """class variable size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be > 0")
        else:
            self.__size = value

    def area(self):
        """Define area"""
        area = self.__size * self.__size ** 2
        return area

    def my_print(self):
        """Print #"""
        if self.__size is 0:
            print()
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print()
