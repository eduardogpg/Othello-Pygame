import pygame

from colors import GREEN

def create_dashboard():
    pos_x = pos_y = 0
    
    dasboard = pygame.sprite.Group()
    
    for _ in range(0, 8):
        for _ in range(0, 8):
            dasboard.add(
                Surface(width=95, height=95, pos_x=pos_x, pos_y=pos_y)
            )
            
            pos_y += 100
        
        pos_y = 0
        pos_x += 100

    return dasboard


class Surface(pygame.sprite.Sprite):
    
    def __init__(self, width, height, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([width, height])
        
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        
        self.rect.x = pos_x
        self.rect.y = pos_y
    
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)