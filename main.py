import sys
import pygame

pygame.init()

from cell import initialize_dashboard

surface = pygame.display.set_mode( ( 800, 800) )
pygame.display.set_caption('Othello')

clock = pygame.time.Clock()

dashboard = initialize_dashboard()

cells = pygame.sprite.Group()
cells.add(dashboard)

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
                    
                    cell.check_box(event.button == 1)
                    cell.validate_neighbours(dashboard)
                    

    cells.draw(surface)
    pygame.display.update()