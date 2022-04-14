import sys
import pygame

pygame.init()

from cell import initialize_dashboard

surface = pygame.display.set_mode( ( 800, 800) )
pygame.display.set_caption('Othello')

clock = pygame.time.Clock()

dasboard = initialize_dashboard()

cells = pygame.sprite.Group()
cells.add(dasboard)


while True:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            for cell in cells:
                if cell.rect.collidepoint(pos) and not cell.token:
                    cell.check(event.button == 1)


    cells.draw(surface)
    pygame.display.update()