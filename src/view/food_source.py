import pygame
from .view_element import ViewElement
from math import sqrt


class FoodSource(ViewElement):
    def __init__(self, view, identifier, x, y, width, height, radius=0, color=pygame.Color("white"),
                 value=100, max_value=100, shape='square', has_image=True, image_path='src/view/images/sugar_cube.png'):
        super(FoodSource, self).__init__(view, identifier, x, y, width, height)
        self.color = color
        self.radius = radius
        self.shape = shape
        self.has_image = has_image
        self.image_path = image_path
        self.value = value
        self.max_value = max_value
        if self.has_image:
            self.image = pygame.image.load(self.image_path)

    def draw(self):
        relative_width = int(self.width * sqrt(self.value / self.max_value))
        relative_height = int(self.height * sqrt(self.value / self.max_value))

        if self.shape == 'circle':
            relative_radius = self.width * self.value / self.max_value
            pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), relative_radius)
        elif self.shape == 'square':
            pygame.draw.rect(self.view.screen, self.color, (self.x, self.y, relative_width, relative_height))
        if self.has_image:
            image = pygame.transform.scale(self.image, (relative_width, relative_height))
            self.view.screen.blit(image, (self.x, self.y, relative_width, relative_height))
