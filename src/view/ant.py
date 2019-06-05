import pygame
import math
from .view_element import ViewElement


class Ant(ViewElement):
    def __init__(self, view, identifier, x, y, color):
        super(Ant, self).__init__(view, identifier, x, y, width=64, height=64)
        self.color = color
        self.direction = [0., 0.]
        self.has_food = False
        name = "_".join((str(c) for c in color))
        self.img = pygame.image.load("src/view/images/219_95_87_scout.png")
        
        self.rotation = 0

    def draw(self):
        rotation = math.atan2(self.direction[0], self.direction[1]) * (180 / math.pi) + 180
        self.rotation += 5
        
        loc = self.img.get_rect().center
        rot_sprite = pygame.transform.rotate(image, angle)
        rot_sprite.get_rect().center = loc
    
        pivot = pygame.math.Vector2(self.width/2, -self.height/2)
        pivot_rotate = pivot.rotate(self.rotation)
        pivot_move = pivot_rotate - pivot
        
        origin = (self.x - pivot_move[0], self.y + pivot_move[1])
        
        img = pygame.transform.rotate(self.img, self.rotation)
        self.view.screen.blit(img, origin)
