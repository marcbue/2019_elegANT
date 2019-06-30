import pygame
import math
from .view_element import ViewElement


class Scout(ViewElement):
    def __init__(self, view, identifier, x, y, color, direction, health):
        super(Scout, self).__init__(view, identifier, x, y, width=64, height=64)
        self.z_index = 9
        self.direction = direction
        self.health = health
        self.has_food = False
        self.color = color
        name = "_".join((str(c) for c in self.color))
        self.img = pygame.image.load(f"src/view/images/{name}_scout.png")

    def draw(self):
        ant_img = self.img

        rotation = math.atan2(self.direction[0], self.direction[1]) * (180 / math.pi) * -1
        ant_img = pygame.transform.rotate(ant_img, rotation)
        loc = ant_img.get_rect().center
        loc = (self.x - (loc[0]), self.y - (loc[1]))

        self.view.screen.blit(ant_img, loc)
