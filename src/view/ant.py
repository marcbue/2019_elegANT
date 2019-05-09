import pygame
from view_element import ViewElement


class Ant(ViewElement):
    def __init__(self, view, identifier, x, y, radius, color):
        super(Ant, self).__init__(view, identifier, x, y, width=radius * 2, height=radius * 2)
        self.color = color
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), self.radius)

    def event_handler(self, event):
        pass
