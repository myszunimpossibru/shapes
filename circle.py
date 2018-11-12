from shape import Shape
import numpy as np
import pygame


class Circle(Shape):
    """
    Class for creating the circle

    Parameters:
        pos: tuple
            Tuple of form (x, y) describing the position of the circle on the screen.
            Reminder: PyGame sets point (0, 0) as the upper left corner and the point with highest value of coordinates
                      as the  lower right corner.
        r: integer
            Radius of the circle.
        scale: integer (default scale=50)
            Value used for scaling the shape while drawing. In default case 1 unit is equal to 50 pixels.
    """

    r = None

    def __init__(self, pos, r, scale=50):
        super().__init__(pos, scale)
        self.r = r

        if r <= 0:
            raise ValueError("Radius cannot be zero or negative.")

    def area(self):
        return self.r * np.pi ** 2

    def perimeter(self):
        return 2 * np.pi * self.r

    def __str__(self):
        return "Circle with radius {}".format(self.r)

    def __repr__(self):
        return "Circle({}, {})".format(self.pos, self.r)

    def draw(self, screen):
        return pygame.draw.circle(screen, (255, 255, 255), self.pos, self.r * self.scale)
