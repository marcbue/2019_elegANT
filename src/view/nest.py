import pygame
from view_element import ViewElement


class Nest(ViewElement):

    def __init__(self, view, identifier, x, y, radius, color):
        super(Nest, self).__init__(view, identifier, x, y, width=radius * 2, height=radius * 2)
        self.color = color
        self.radius = radius
        self.on('click', self.click_event)

    def draw(self):
        pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), self.radius)

    def event_handler(self, event):
        pos = self.view.mouse_pos

        if self.x + self.radius > pos[0] > self.x - self.radius and self.y + self.radius > pos[1] > \
                self.y - self.radius:

            if "click" in self.events and event.type == pygame.MOUSEBUTTONDOWN:
                for fnct, args in self.events["click"]:
                    fnct(**args)

    def click_event(self):
        pass
