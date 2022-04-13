import sys
import pygame

pygame.init()

surface = pygame.display.set_mode( (  800, 800) )
pygame.display.set_caption('Example')

clock = pygame.time.Clock()

while True:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()