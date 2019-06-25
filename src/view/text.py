import pygame
from .ui_element import UIElement


class Text(UIElement):
    def __init__(self, view, identifier, x, y, width, height, color=(0, 0, 0)):
        pygame.init()
        super(Text, self).__init__(view, identifier, x, y, width, height)
        self.color = color

    def set_text(self, text):
        self.text = text
        self.fontsize = self.height
        largeText = pygame.font.Font('Garamond_Regular.ttf', self.fontsize)
        self.TextSurf = largeText.render(self.text, True, self.color)
        self.TextRect = self.TextSurf.get_rect()
        self.TextRect.topleft = (self.x, self.y)
        self.view.screen.blit(self.TextSurf, self.TextRect)

    def draw(self):
        super(Text, self).draw()
        self.fontsize = self.height
        largeText = pygame.font.Font('Garamond_Regular.ttf', self.fontsize)
        self.TextSurf = largeText.render(self.text, True, self.color)
        self.TextRect = self.TextSurf.get_rect()
        self.TextRect.topleft = (self.x, self.y)
        self.view.screen.blit(self.TextSurf, self.TextRect)

    def event_handler(self, event):
        pass
