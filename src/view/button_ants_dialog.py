import math
import pygame
from .button import Button


class AntsDialogButton(Button):
    def __init__(self, *args, **kwargs):
        super(AntsDialogButton, self).__init__(*args, **kwargs)

        self.counter = 0
        self._loading_angle = 0

    def draw(self):
        rect = [self.x, self.y, self.width, self.height]
        self.view.screen.fill((0, 0, 0), rect, 2)

        largeText = pygame.font.SysFont('centuryschoolbook', 120)
        TextSurf = largeText.render("+", True, (200, 56, 56))
        TextRect = TextSurf.get_rect()
        TextRect.center = (self.x + math.floor(self.width / 2), self.y + math.floor(self.height / 2) - 5)
        self.view.screen.blit(TextSurf, TextRect)
