#!/usr/bin/python3
"""This module defines a Square class with size validation and area method."""


class Square:
    """A class that defines a square and can compute its area."""

    def __init__(self, size=0):
        """Initialize the square with a given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
