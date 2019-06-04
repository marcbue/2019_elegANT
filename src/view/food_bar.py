import pygame
from .view_element import ViewElement


class FoodBar(ViewElement):
    def __init__(self, view, identifier, x, y, width, height, color=pygame.Color("white"),
                 value=100, max_value=1000, shape='square'):
        super(FoodBar, self).__init__(view, identifier, x, y, width, height)
        self.color = color
        self.color2 = pygame.Color("gray")
        self.shape = shape
        self.value = value
        self.max_value = max_value

    def draw(self):
        relative_width = int(min(self.width - 10, (self.width - 10) * (self.value / self.max_value)))

        pygame.draw.rect(self.view.screen, self.color2, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.view.screen, self.color,
                         (self.x + 5, self.y + 5, relative_width, self.height - 10))

        txt_name = self.view.FONT.render(f"{self.value}/{self.max_value}", True, pygame.Color("black"))
        txt_width, txt_height = self.view.FONT.size(f"{self.value}/{self.max_value}")
        self.view.screen.blit(txt_name, (self.x + self.width / 2 - txt_width / 2,
                                         self.y + self.height / 2 - txt_height / 2))
