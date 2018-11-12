from shape import Shape
import numpy as np
import pygame


class Parallelogram(Shape):
    """
    Class for creating the Parallelogram

    Parameters:
        pos: tuple
            Tuple of form (x, y) describing the position of the circle on the screen.
            Reminder: PyGame sets point (0, 0) as the upper left corner and the point with highest value of coordinates
                      as the  lower right corner.
        a: integer
            Length of the first side.
        b: integer
            Length of the second side.
        alpha: degrees
            Angle between two sides.
    """

    a = None
    b = None
    alpha = None
    __deg = None

    def __init__(self, pos, a, b, alpha, scale=50):
        super().__init__(pos, scale)
        self.a = a
        self.b = b

        if alpha >= 90 or alpha <= 0:
            raise ValueError("The angle has to be between 0° and 90° degrees")

        self.__deg = alpha
        self.alpha = np.pi * alpha / 180

    def area(self):
        return self.a * self.b * np.sin(self.alpha)

    def perimeter(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        return "Parallelogram with dimensions of {} x {} and angle {} between sides.".format(self.a, self.b, self.__deg)

    def __repr__(self):
        return "Parallelogram({}, {}, {}, {})".format(self.pos, self.a, self.b, self.__deg)

    def draw(self, screen):
        h = np.ceil(self.b * np.sin(self.alpha)) * self.scale
        dx = np.ceil(self.b * np.cos(self.alpha)) * self.scale
        points = [self.pos, (self.pos[0] + self.a * self.scale, self.pos[1]), (self.pos[0] + self.a * self.scale + dx,
                  self.pos[1] - h), (self.pos[0] + dx, self.pos[1] - h)]
        return pygame.draw.polygon(screen, (255, 255, 255), points)


class CrazyDiamond(Parallelogram):
    """
    Parallelogram with even sides

    See help of Parallelogram class for more information.
    """

    def __init__(self, a, alpha):
        super().__init__(a, a, alpha)

    def __repr__(self):
        return "Rhombus({}, {}, {})".format(self.pos, self.a, self.alpha)
