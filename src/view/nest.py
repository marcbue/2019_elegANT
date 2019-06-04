import pygame
from .view_element import ViewElement
from math import sqrt


class Nest(ViewElement):
    def __init__(self, view, identifier, x, y, radius, color, value=1000, max_value=1000, shape='square',
                 has_image=True, image_path='src/view/images/nest_hole.png'):
        super(Nest, self).__init__(view, identifier, x, y, width=radius * 2, height=radius * 2)
        self.color = color
        self.radius = radius
        self.shape = shape
        self.value = value
        self.max_value = max_value
        self.has_image = has_image
        self.image_path = image_path
        if self.has_image:
            self.image = pygame.image.load(self.image_path)

    def draw(self):
        relative_width = int(self.width * sqrt(self.value / self.max_value))
        relative_height = int(self.height * sqrt(self.value / self.max_value))

        if self.shape == 'circle':
            relative_radius = int(self.radius * 2 * sqrt(self.value / self.max_value))
            pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), relative_radius)
        elif self.shape == 'square':
            pygame.draw.rect(self.view.screen, self.color, (self.x, self.y, relative_width, relative_height))
        if self.has_image:
            self.color = pygame.Color("white")
            image = pygame.transform.scale(self.image, (relative_width, relative_height))
            self.view.screen.blit(image, (self.x, self.y, relative_width, relative_height))
