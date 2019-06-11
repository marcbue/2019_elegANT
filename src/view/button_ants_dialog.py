import math
import pygame
from .button import Button


class AntsDialogButton(Button):
    def draw(self):
        largeText = pygame.font.SysFont('centuryschoolbook', 120)
        TextSurf = largeText.render("+", True, (200, 56, 56))
        TextRect = TextSurf.get_rect()
        TextRect.center = (self.x + math.floor(self.width / 2), self.y + math.floor(self.height / 2) - 5)
        self.view.screen.blit(TextSurf, TextRect)
