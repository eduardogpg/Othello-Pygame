import sys
import pygame

from colors import *
from constants import *

from cell import create_dashboard
from cell import initialize_dashboard

pygame.init()

clock = pygame.time.Clock()

surface = pygame.display.set_mode( (800, 850) )
pygame.display.set_caption(TITLE)

menu = pygame.Surface((800, 50))
game = pygame.Surface((800, 800))

font = pygame.font.SysFont(FONT, FONT_SIZE)

dashboard = initialize_dashboard()

cells = pygame.sprite.Group()
cells.add(dashboard)

turn_player1 = True

player1_tokens = 2
player2_tokens = 2

while True:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            
            for cell in cells:
                
                if cell.rect.collidepoint( (pos[0], pos[1] - 50)) and not cell.token:
                    
                    if cell.neighbours(dashboard):
                        
                        cell.check_box(turn_player1)
                        cell.validate_neighbours(dashboard)
                        
                        player1_tokens = sum([ 1 for cell in cells if cell.token and cell.player1 ])
                        player2_tokens = sum([ 1 for cell in cells if cell.token and not cell.player1 ])
                        
                        turn_player1 = not turn_player1
                    
        
    menu.fill(BLACK)
    
    text1 = font.render(f'Blancas: {player1_tokens}', True, WHITE)
    text2 = font.render(f'Negras: {player2_tokens}', True, WHITE)
    
    menu.blit(text1, (text1.get_width(), 25 - text1.get_height() // 2) )
    menu.blit(text2, (800 - (text2.get_width()) * 2, 25 - text2.get_height() // 2) )
    
    cells.draw(game)
    
    surface.blit(menu, (0, 0))
    surface.blit(game, (0, 50))
    
    pygame.display.update()