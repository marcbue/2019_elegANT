import pygame
from .ui_element import UIElement


class Button(UIElement):
    def __init__(self, view, identifier, x, y, width, height, radius, color1, color2,
                 shape='circle', has_image=False, image_path=''):
        super(Button, self).__init__(view, identifier, x, y, width, height)
        self.color1 = color1
        self.color2 = color2
        self.color = color1
        self.radius = radius
        self.shape = shape
        self.has_image = has_image
        self.image_path = image_path

    def change_color(self, new_color):
        self.color = new_color

    def draw(self):
        if self.shape == 'circle':
            pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), self.radius)
            if self.has_image is True:
                image = pygame.transform.scale(pygame.image.load(self.image_path), (self.width, self.height))
                self.view.screen.blit(image,
                                      pygame.Rect(self.x - (self.width // 2), self.y - (self.height // 2), self.width,
                                                  self.height))
        elif self.shape == 'square':
            pygame.draw.rect(self.view.screen, self.color, (self.x, self.y, self.width, self.height))

            if self.has_image is True:
                image = pygame.transform.scale(pygame.image.load(self.image_path), (self.width, self.height))
                self.view.screen.blit(image, pygame.Rect(self.x, self.y, self.width, self.height))

