import sys
import pygame

pygame.init()

from surface import Surface
from surface import create_dashboard

surface = pygame.display.set_mode( (  795, 795) )
pygame.display.set_caption('Example')

clock = pygame.time.Clock()

surfaces = create_dashboard()

print(len(surfaces))

while True:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    surfaces.draw(surface)
    pygame.display.update()