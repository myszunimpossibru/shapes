# coding: utf8
import rectangles
import circle
import triangle
import parallelogram
import numpy as np
import pygame

#Defining the shapes
par1 = parallelogram.Parallelogram((24, 500), 2, 4, 45)
rect1 = rectangles.Rectangle((20, 10), 2, 3)
cir1 = circle.Circle((400, 50), 1)
tr1 = triangle.Triangle((300, 500), np.array([0, 2]), np.array([2, 0]))

#Initalization of PyGame
pygame.init()
running = True
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Shape drawing")
clock = pygame.time.Clock()

#PyGame's main loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    par1.draw(screen)
    rect1.draw(screen)
    cir1.draw(screen)
    tr1.draw(screen)
    pygame.display.update()
    clock.tick(60)
