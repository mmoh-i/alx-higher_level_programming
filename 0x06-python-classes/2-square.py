#!/usr/bin/python3
<<<<<<< HEAD

=======
"""Square module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Constructor
        Args:
            size: length of side of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: If size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
>>>>>>> dfd8d724d138b6aec5651e27ef45b493e1d498cb
