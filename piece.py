import pygame

class Piece(pygame.sprite.Sprite)

    def __init__(self, width, height, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([width, height])
        
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        
        self.rect.x = pos_x
        self.rect.y = pos_y