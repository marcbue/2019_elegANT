import pygame
from .ui_element import UIElement


class Ant(UIElement):
    def __init__(self, view, identifier, x, y, radius, color, shape='circle'):
        super(Ant, self).__init__(view, identifier, x, y, width=radius * 2, height=radius * 2)
        self.color = color
        self.radius = radius
        self.shape = shape

    def draw(self):
        pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), self.radius)
