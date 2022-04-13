import sys
import pygame

pygame.init()

from surface import Surface
from surface import create_dashboard

surface = pygame.display.set_mode( (  795, 795) )
pygame.display.set_caption('Othello')

clock = pygame.time.Clock()

surfaces = create_dashboard()

while True:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            for s in surfaces:
                if s.rect.collidepoint(pos):
                    s.draw_circle()


    surfaces.draw(surface)
    pygame.display.update()