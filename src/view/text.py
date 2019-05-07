import pygame
from view_element import ViewElement


class Text(ViewElement):
    def __init__(self, view, identifier, x, y, width, height, fontsize):
        pygame.init()
        super(Text, self).__init__(view, identifier, x, y, width, height)
        self.fontsize = fontsize

    def set_text(self, text):
        self.text = text
        largeText = pygame.font.SysFont('centuryschoolbook', self.fontsize)
        self.TextSurf = largeText.render(self.text, True, (56, 56, 56))
        self.TextRect = self.TextSurf.get_rect()
        self.TextRect.center = (self.x, self.y)

    def draw(self):
        self.view.screen.blit(self.TextSurf, self.TextRect)

    def event_handler(self, event):
        pass
