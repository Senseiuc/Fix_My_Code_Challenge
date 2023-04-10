#!/usr/bin/python3
"""
A SQUARE MODULE
"""


class Square():

    """
    A class Square that represensts a square

    ...

    Attributes
    ----------
    width : int or float
        the width of the square
    height : int or float
        the height of the square
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Parameters
        ----------
        args : list
            the list of arguments
        kwargs : dict
            the dictionary of values
        """
        for i in range(len(args)):
            """ loop through the arguments"""
            if not isinstance(args[i], int):
                raise ValueError("Enter a integer or float")
            if i % 2 == 0:
                setattr(self, 'width', args[0])
            else:
                setattr(self, 'height', args[1])
        for key, value in kwargs.items():
            """ loop through the kwargs dictionary"""
            if not isinstance(value, int):
                raise ValueError("Enter a integer or float")
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimiter_of_my_square(self):
        """ perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ string representation"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimiter_of_my_square())
