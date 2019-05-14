import pygame
from ui_element import UIElement


class Nest(UIElement):

    def __init__(self, view, identifier, x, y, radius, color, shape='circle', active=False):
        super(Nest, self).__init__(view, identifier, x, y, width=radius * 2, height=radius * 2)
        self.color = color
        self.active_color = pygame.Color("orange")
        self.radius = radius
        self.shape = shape
        self.active = active
        self.on('click', self.click)

    def draw(self):
        if self.active:
            pygame.draw.circle(self.view.screen, self.active_color, (self.x, self.y), self.radius + 10)
        pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), self.radius)

    def click(self):
        self.active = True

