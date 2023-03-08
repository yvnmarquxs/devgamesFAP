import pygame
import sys
from pygame.locals import *


pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Japão')

display.fill(
    (
        255,
        255,
        255
    ))

clock = pygame.time.Clock()

x, y = display.get_size()

pygame.draw.circle(display, (255, 0, 0), (x/2,y/2), 100)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(1)
    pygame.display.update()