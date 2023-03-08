import pygame
import sys
from pygame.locals import *

pygame.init()


displaygame = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Brasil')


x, y = displaygame.get_size()

displaygame.fill((22, 150, 3))
pygame.draw.polygon(displaygame, (219, 242, 10), ((55, y/2), (x/2, 55), (x-55, y/2), (x/2, y-55)))
pygame.draw.circle(displaygame, (34, 28, 214, 100), (x/2, y/2), 140)

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 

