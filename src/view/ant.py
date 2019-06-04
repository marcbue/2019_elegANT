import pygame
from .view_element import ViewElement
from math import sqrt


class Ant(ViewElement):
    def __init__(self, view, identifier, x, y, radius, color, health=10, max_health=10, shape='square',
                 has_image=True, image_path='src/view/images/ant.png'):
        super(Ant, self).__init__(view, identifier, x, y, width=radius * 2, height=radius * 2)
        self.color = color
        self.radius = radius
        self.shape = shape
        self.health = health
        self.max_health = max_health
        self.has_image = has_image
        self.image_path = image_path
        if self.has_image:
            self.image = pygame.image.load(self.image_path)

    def draw(self):
        relative_width = int(self.width * sqrt(self.health / self.max_health))
        relative_height = int(self.height * sqrt(self.health / self.max_health))

        if self.has_image:
            image = pygame.transform.scale(self.image, (relative_width, relative_height))
            self.view.screen.blit(image, (self.x, self.y, relative_width, relative_height))
        elif self.shape == 'circle':
            relative_radius = int(self.radius * 2 * sqrt(self.health / self.max_health))
            pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), relative_radius)
        elif self.shape == 'square':
            pygame.draw.rect(self.view.screen, self.color, (self.x, self.y, relative_width, relative_height))
