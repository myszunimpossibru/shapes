# coding: utf8


class Shape(object):
    """
    Base class for all shapes.
    """

    pos = None
    scale = None

    def __init__(self, pos, scale):
        self.pos = pos
        self.scale = scale

    def area(self):
        """
        Abstract method returning area of a shape.
        """

    def perimeter(self):
        """
        Abstract method returning shape perimeter.
        """

    def summary(self):
        """
        Return summary of a shape.
        """
        return {
            'area': self.area(),
            'perimeter': self.perimeter()
        }

    def draw(self, screen):
        """
        Draws the given shape
        """