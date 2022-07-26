#!/usr/bin/python3
class Rectangle:
    """Defines a rectangle class"""
    def __init__(self, width = 0, height = 0):
        """Initializes a new rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.

        """
        self.width = width
        self.height = height

    def get_width(self):
        """Get/Set the width of the rectangle"""
        return self.__width
    
    def set_width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        #self.__width = value

    def get_height(self):
        """Get/Set the height of the rectangle"""
        return self.__height
    
    def set_width(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height msut be >= 0")
        #self.__height = value
