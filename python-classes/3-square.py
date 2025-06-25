#!/usr/bin/python3
"""This module defines a Square class with getter and setter for size."""


class Square:
    """A class that defines a square with access control on size."""

    def __init__(self, size=0):
        """Initialize the square with a given size using setter."""
        self.size = size  # Uses the property setter

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
