import pygame

from colors import GREEN
from colors import WHITE
from colors import BLACK

def create_dashboard():
    pos_x = pos_y = 0
    dasboard = pygame.sprite.Group()
    
    for _ in range(0, 8):
        for _ in range(0, 8):
            dasboard.add(width=95, height=95, pos_x=pos_x, pos_y=pos_y))
            pos_y += 100
        
        pos_y = 0
        pos_x += 100

    return dasboard


class Surface(pygame.sprite.Sprite):
    
    def __init__(self, width, height, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.white = True
        
        self.width = width
        self.height = height
        self.dimension = (self.width, self.height)
        
        self.image = pygame.Surface(self.dimension)
        
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        
        self.rect.x = pos_x
        self.rect.y = pos_y
    
        
    def draw_circle(self):
        pos =  (self.width // 2, self.height // 2)
        pygame.draw.circle(self.image, self.color, pos, 40)
    
    
    @property
    def color(self):
        if self.white:
            return WHITE

        return BLACK
        