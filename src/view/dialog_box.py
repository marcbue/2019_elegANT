from .ui_element import UIElement
import pygame


class DialogBox(UIElement):
    def __init__(self, view, identifier, x, y, width, height, background_color=pygame.Color("grey"), shape="square"):
        super(DialogBox, self).__init__(view, identifier, x, y, width, height)
        self.relativex = self.xc
        self.relativey = self.yc
        self.relativew = self.w
        self.relativeh = self.h
        self.rect = pygame.Rect(self.relativex, self.relativey, self.relativew, self.relativeh)
        self.background_color = background_color
        self.shape = shape

    def draw(self):
        pass
