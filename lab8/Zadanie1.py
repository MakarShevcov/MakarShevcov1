import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (255, 0, 0), (120, 135), 25)
circle(screen, (0, 0, 0), (120, 135), 10)
circle(screen, (255, 0, 0), (275, 135), 25)
circle(screen, (0, 0, 0), (275, 135), 10)
color = (90, 30, 30)
line(screen, color, (110, 90), (170, 120), 10)
line(screen, color, (280, 90), (220, 120), 10)
color = (0, 0, 0)
line(screen, color, (110, 250), (280, 250), 30)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
