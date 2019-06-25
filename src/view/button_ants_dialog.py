import math
import pygame
from .button import Button


class AntsDialogButton(Button):
    def draw(self):
        self.fontsize = int(self.width * 1.5)
        largeText = pygame.font.SysFont('Garmond_Bond.ttf', self.fontsize)
        TextSurf = largeText.render("+", True, self.color)
        TextRect = TextSurf.get_rect()
        TextRect.center = (self.x + math.floor(self.width / 2), self.y + math.floor(self.height / 2) - 5)
        self.view.screen.blit(TextSurf, TextRect)
