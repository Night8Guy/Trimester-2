#!/usr/bin/python3
"""This module writes a class 'Square'.
This class will initialize a size for Square."""


class Square:
    """Class that initializes size as a private instance attribute"""
    def __init__(self, size):
        self.__size = size
        """init func initializes Square object and gives it a size"""
