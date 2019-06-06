import pygame
from .view_element import ViewElement

class Nest(ViewElement):
    def __init__(self, view, identifier, x, y, max_radius, color, value, max_value=500):
        super(Nest, self).__init__(view, identifier, x, y, width=0, height=0)
        self.z_index = 2
        self.max_radius = max_radius
        self.value = value
        self.max_value = max_value
        self.width = self.height = self._update_width_height()
        name = "_".join((str(c) for c in color))
        self.image = pygame.image.load(f"src/view/images/{name}_nest.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self):
        self.width = self.height = self._update_width_height()
        image = pygame.transform.scale(self.image, (self.width, self.height))
        self.view.screen.blit(image, (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height))
        
    def _update_width_height(self):
        return int(((self.max_radius * 2 - 80) * self.value / self.max_value) + 80)
