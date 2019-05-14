import pygame
from ui_element import UIElement


class Button(UIElement):
    def __init__(self, view, identifier, x, y, width, height, radius, color1, color2, shape='circle'):
        super(Button, self).__init__(view, identifier, x, y, width, height)
        self.color1 = color1
        self.color2 = color2
        self.color = color1
        self.radius = radius
        self.shape = shape
        self.width = width
        self.height = height

    def change_color(self, new_color):
        self.color = new_color

    def draw(self):
        if self.shape == 'circle':
            pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), self.radius)
        elif self.shape == 'square':
            pygame.draw.rect(self.view.screen, self.color, (self.x, self.y, self.width, self.height))
        else:
            print('not valid')
