class Rectangle:
    """defines a class Rectangle"""

    def __init__(self, width = 0, height = 0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        """setting the height property setter"""
        if not isinstance(value, int):
            raise TypeError("height msut be an integer")
        if height < 0:
            raise ValueError("height must be  >= 0")
    def area(self):
        """The Area of a rectangle"""
        return (self.__width * self.__height)
    def perimeter(self):
        """The perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height))
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = list()
        for cols in range(self.__height):
            [rect.append("#") for row in range(self.__width)]
            if cols != self.__height - 1:
                rect.append("\n")
            return ("".join(rect))
    def __repr__(self):
        """Returns the string representation of the Rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += "," + str(self.__width) + ")"
        return (rect)
