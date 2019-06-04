import pygame
from .view_element import ViewElement
from math import sqrt


class Ant(ViewElement):
    def __init__(self, view, identifier, x, y, radius, color, health=10, max_health=10, shape='circle'):
        super(Ant, self).__init__(view, identifier, x, y, width=radius * 2, height=radius * 2)
        self.color = color
        self.radius = radius
        self.shape = shape
        self.health = health
        self.max_health = max_health

    def draw(self):
        relative_radius = int(self.radius * sqrt(self.health / self.max_health))
        pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), relative_radius)
