#!/usr/bin/python3
"""Square Module """


class Square():
    """Creating Square class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """instantiation of class"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ perimeter of square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ format representation"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ create an object and calculate"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
