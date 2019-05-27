import pygame
from .ui_element import UIElement


class Text(UIElement):
    def __init__(self, view, identifier, x, y, width, height):
        pygame.init()
        super(Text, self).__init__(view, identifier, x, y, width, height)

        self.x = self.xc
        self.y = self.yc
        self.width = self.w
        self.height = self.h
        self.fontsize = self.width * self.height

    def set_text(self, text):
        self.text = text
        largeText = pygame.font.Font('Garamond_Regular.ttf', self.fontsize)
        self.TextSurf = largeText.render(self.text, True, (0, 0, 0))
        self.TextRect = self.TextSurf.get_rect()
        self.TextRect.center = (self.x, self.y)

    def draw(self):
        self.view.screen.blit(self.TextSurf, self.TextRect)

    def event_handler(self, event):
        pass
