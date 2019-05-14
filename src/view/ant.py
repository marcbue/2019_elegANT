import pygame
from ui_element import UIElement


class Ant(UIElement):
    def __init__(self, view, identifier, x, y, radius, color, shape='circle'):
        super(Ant, self).__init__(view, identifier, x, y, width=radius * 2, height=radius * 2)
        self.color = color
        self.active_color = pygame.Color("orange")
        self.radius = radius
        self.shape = shape
        self.active = False
        self.on('click', self.click)

    def click(self):
        self.active = True

    def draw(self):
        if self.active:
            pygame.draw.circle(self.view.screen, self.active_color, (self.x, self.y), self.radius + 5)
        pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), self.radius)
