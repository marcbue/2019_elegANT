import pygame
from .ui_element import UIElement


class InputBox(UIElement):
    def __init__(self, view, identifier, x, y, width, height, text, shape='square'):
        UIElement.__init__(self, view, identifier, x, y, width, height)
        self.text = text
        self.active = False
        self.shape = shape
        self.color = self.view.background_color
        self.textcolor = (0, 0, 0)
        self.largeText = pygame.font.Font('Garamond_Regular.ttf', int(0.70 * self.height))
        self.txt_surface = self.largeText.render(self.text, True, (190, 190, 190))
        self.on("click", self.click)
        self.on("keyret", self.key_ret)
        self.on("keyback", self.key_back)
        self.on("keychar", self.key_char)

    def click(self):
        self.text = ''
        self.active = True
        self.txt_surface = self.largeText.render(self.text, True, self.color)

    def key_ret(self):
        self.active = False

    def key_back(self):
        self.text = self.text[:-1]

    def key_char(self, char):
        self.text += char

    def draw(self):
        super(InputBox, self).draw()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.linerect = pygame.Rect(self.x, self.y + 0.90 * self.height, self.width, 2)
        self.largeText = pygame.font.Font('Garamond_Regular.ttf', int(0.70 * self.height))
        self.txt_surface = self.largeText.render(self.text, True, self.textcolor)

        width = max(self.width, self.txt_surface.get_width() + 0.10 * self.width)
        self.rect.width = width
        self.linerect.width = width

        self.view.screen.fill(self.view.background_color, self.rect)
        self.view.screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(self.view.screen, self.color, self.rect, 2)
        pygame.draw.rect(self.view.screen, self.textcolor, self.linerect, 2)
