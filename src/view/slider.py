from .ui_element import UIElement
import pygame


class Slider(UIElement):
    def __init__(self, view, identifier, x, y, width, height, max_value=100, min_value=0, default_value=50,
                 shape="square", name="val:"):
        super(Slider, self).__init__(view, identifier, x, y, width, height)

        self.identifier = identifier
        self.value = default_value
        self.max_value = max_value
        self.min_value = min_value
        self.shape = shape
        self.name = name
        self.on("click", self.click)

    def click(self):
        mouse_pos_x, mouse_pos_y = self.view.mouse_pos
        relative_pos = (mouse_pos_x - self.x) / self.width
        self.value = relative_pos * (self.max_value - self.min_value) + self.min_value
        self.view.event_dict.update({f"slider_{self.identifier}": self.value})

    def draw(self):
        super(Slider, self).draw()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        slider_rect = pygame.Rect(self.x, self.y + self.height // 2 - 3, self.width, 6)
        pygame.draw.rect(self.view.screen, pygame.Color("black"), slider_rect, 0)
        relative_value = self.value / (self.max_value - self.min_value)
        pygame.draw.circle(self.view.screen, pygame.Color("black"),
                           (int(self.x + self.width * relative_value), self.y + self.height // 2), 10)

        # TODO do we want to display value? (not wanted as feature)
        # txt_value = self.view.FONT.render(f"{self.value:.0f}", True, pygame.Color("black"))
        # self.view.screen.blit(txt_value, (self.rect.x + 5, self.rect.y + self.height))

        txt_name = self.view.FONT.render(f"{self.name}", True, pygame.Color("black"))
        self.view.screen.blit(txt_name, (self.rect.x + 5, self.rect.y - 20))

