from shape import Shape
import numpy as np
import pygame


class Triangle(Shape):
    """
    Class for creating the triangular shape

    Parameters:
        pos: tuple
            Tuple of form (x, y) describing the position of the triangle on the screen.
            Reminder: PyGame sets point (0, 0) as the upper left corner and the point with highest value of coordinates
                      as the  lower right corner.
        a: array
            Components of the first triangle vector
        b: array
            Components of the second triangle vector
        scale: integer (default scale=50)
            Value used for scaling the shape while drawing. In default case 1 unit is equal to 50 pixels.
    """

    a = None
    b = None
    c = None

    def __init__(self, pos, a, b, scale=50):
        super().__init__(pos, scale)
        self.a = a
        self.b = b

        if np.linalg.norm(self.a) == 0 or np.linalg.norm(self.b) == 0:
            raise ValueError("Vectors cannot have zero length.")
        elif np.linalg.norm(np.cross(a, b)) == 0:
            raise ValueError("Vectors cannot have the same direction")

        self.c = a - b

    def area(self):
        return 0.5 * np.linalg.norm(self.a[0] * self.b[1] - self.a[1] * self.b[0])

    def perimeter(self):
        return np.linalg.norm(self.a) + np.linalg.norm(self.b) + np.linalg.norm(self.c)

    def __str__(self):
        return "Triangle with sides a:{}, b:{}, c:{})".format(self.a, self.b, self.c)

    def __repr__(self):
        return "Triangle({}, {}, {})".format(self.pos, self.a, self.b)

    def draw(self, screen):
        points = [self.pos, (self.pos + self.a * self.scale), (self.pos + self.b * self.scale)]
        return pygame.draw.polygon(screen, (255, 255, 255), points)
