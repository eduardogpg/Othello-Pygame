import pygame

from colors import GREEN
from colors import WHITE
from colors import BLACK


def initialize_dashboard():
    dashboard = create_dashboard()
    
    """
    dashboard[3][3].check(False)
    dashboard[3][4].check(True)
    
    dashboard[4][3].check(True)
    dashboard[4][4].check(False)
    """
    
    return dashboard


def create_dashboard():
    dasboard = []
    
    for x in range(0, 8):
        rows = []
        
        for y in range(0, 8):
            cell = Cell(width=100, height=100, pos_x=x, pos_y=y)
            rows.append(cell)
        
        dasboard.append(rows)

    return dasboard


class Cell(pygame.sprite.Sprite):
    
    def __init__(self, width, height, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.player1 = False
        self.token = False
        
        self.width = width
        self.height = height
        
        self.image = pygame.Surface((self.width -2 , self.height - 2))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.rect.x = pos_x * self.width
        self.rect.y = pos_y * self.height
    
    
    def check_box(self, player1=True):
        self.player1 = player1
        self.check()
        

    def validate_neighbours(self, dashboard):
        pass
    
    
    def check_neighbours(self, dashboard, player1, pos_x, pos_y, _x, _y):
        pass


    def check(self):
        self.token = True
        pygame.draw.circle(self.image, self.color, (self.width // 2, self.height // 2), 40)
        
        return self.token
        
    
    @property
    def color(self):
        if self.player1:
            return WHITE

        return BLACK
    
    
    def __str__(self):
        return f'({self.pos_x}-{self.pos_y})'