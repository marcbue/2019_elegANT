import pygame
from .ui_element import UIElement


class InputBox(UIElement):
    def __init__(self, view, identifier, x, y, width, height, color1, color2, text='', shape='square'):
        UIElement.__init__(self, view, identifier, x, y, width, height)

        self.x = self.x1
        self.y = self.y1
        self.width = self.w1
        self.height = self.h1

        print(self.x, self.y, self.width, self.height)

        self.rect = pygame.Rect(x, y, width, height)
        self.color1 = color1
        self.color2 = color2
        self.color = color1
        self.text = text
        self.txt_surface = self.view.FONT.render(text, True, self.color)
        self.active = False
        self.shape = shape
        self.on("click", self.click)
        self.on("keyret", self.key_ret)
        self.on("keyback", self.key_back)
        self.on("keychar", self.key_char)

    def click(self):
        self.active = True

    def key_ret(self):
        self.active = False

    def key_back(self):
        self.text = self.text[:-1]
        self.txt_surface = self.view.FONT.render(self.text, True, self.color1)

    def key_char(self, char):
        self.text += char
        self.txt_surface = self.view.FONT.render(self.text, True, self.color1)

    def draw(self):
        if self.active:
            self.color = self.color2
        else:
            self.color = self.color1

        width = max(250, self.txt_surface.get_width() + 10)
        self.rect.w = width

        self.view.screen.fill(self.view.background_color, self.rect)
        self.view.screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(self.view.screen, self.color, self.rect, 2)
