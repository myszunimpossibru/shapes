# coding: utf8
from shape import Shape
import pygame


class Rectangle(Shape):
    """
    Class for creating the rectangular shape

    Parameters:
        pos: tuple
            Tuple of form (x, y) describing the position of the rectangle on the screen.
            Reminder: PyGame sets point (0, 0) as the upper left corner and the point with highest value of coordinates
                      as the  lower right corner.
        a: integer
            Length of the first side
        b: integer
            Length of the second side
        scale: integer (default scale=50)
            Value used for scaling the shape while drawing. In default case 1 unit is equal to 50 pixels.
    """

    a = None
    b = None

    def __init__(self, pos, a, b, scale=50):
        super().__init__(pos, scale)
        self.a = a
        self.b = b

        if self.a <= 0 or self.b <= 0:
            raise ValueError("Size cannot be negative or zero")

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        return "Rectangle of dimensions {} x {}".format(self.a, self.b)

    def __repr__(self):
        return "Rectangle({}, {}, {})".format(self.pos, self.a, self.b)

    def draw(self, screen):
        points = [self.pos, (self.pos[0] + self.a * self.scale, self.pos[1]), (self.pos[0] + self.a * self.scale, self.pos[1] + self.b * self.scale), \
                  (self.pos[0], self.pos[1] + self.b * self.scale)]
        return pygame.draw.polygon(screen, (255, 255, 255), points)


class Square(Rectangle):
    """
    Rectangle with even sides.

    See help of Rectangle class for more information.
    """

    def __init__(self, a):
        super().__init__(a, a)

    def __repr__(self):
        return "Square({}, {})".format(self.pos, self.a)
