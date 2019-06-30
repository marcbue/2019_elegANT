from .ui_element import UIElement
import pygame


class DialogBox(UIElement):
    def __init__(self, view, identifier, x, y, width, height, background_color=pygame.Color("grey"), shape="square"):
        super(DialogBox, self).__init__(view, identifier, x, y, width, height)
        self.background_color = background_color
        self.shape = shape

    def draw(self):
        super(DialogBox, self).draw()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pass
