import pygame

from colors import *

def initialize_dashboard():
    dashboard = create_dashboard()
    
    dashboard[3][3].check_box(False)
    dashboard[3][4].check_box(True)
    
    dashboard[4][3].check_box(True)
    dashboard[4][4].check_box(False)
    
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
        self.__check()


    def validate_neighborhoods(self, dashboard):
        for x in range(-1, 2):
            for y in range(-1, 2):
                self.check_neighborhoods(dashboard, self.player1, self.pos_x, self.pos_y, x, y)


    def check_neighborhoods(self, dashboard, player1, pos_x, pos_y, _x, _y):
        try:
            pos_x = pos_x + _x
            pos_y = pos_y + _y
            
            cell = dashboard[pos_x][pos_y]
            if cell.token:
                
                if cell.player1 == player1:
                    return True
                
                if cell.check_neighborhoods(dashboard, player1, pos_x, pos_y, _x, _y):
                    cell.check_box(player1)
                    return True
            
            return None
        
        except Exception as err:
            return None
    
    
    def neighborhoods(self, cells):
        neighborhoods = list()
        
        for x in range(self.pos_x - 1, self.pos_x + 2):
            for y in range(self.pos_y - 1, self.pos_y + 2):
               
                cell = cells[x][y]
                if (x >= 0 and y >= 0) and (x < len(cells) and y < len(cells[0])) and cell.token:
                    neighborhoods.append(cells[x][y]) 

        return neighborhoods

    @property
    def color(self):
        if self.player1:
            return WHITE

        return BLACK
    
    
    def __check(self):
        self.token = True
        pygame.draw.circle(self.image, self.color, (self.width // 2, self.height // 2), 40)


    def __str__(self):
        return f'({self.pos_x}-{self.pos_y})'