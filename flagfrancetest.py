import pygame
import sys
from pygame.locals import *

pygame.init()

# Display:
displaygame = pygame.display.set_mode((800, 600))
pygame.display.set_caption('França')

# Desenhar:
displaygame.fill([255, 255, 255])
                #    x  y   w    h          (w = Largura, h= Altura)
rectum = pygame.Rect(0, 0, 260, 600)
pygame.draw.rect(displaygame, (20, 40, 196), rectum)

rectdois = pygame.Rect(555, 0, 300, 600)
pygame.draw.rect(displaygame, (230, 7, 7), rectdois)

pygame.display.update()

# GameLoop:
while True:
    for event in pygame.event.get():
        #print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 

