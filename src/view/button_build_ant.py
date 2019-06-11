import math
import pygame
from .button import Button

from src.settings import all_params


PI = math.pi
STATE_BUTTON = 'add'
STATE_LOADING = 'loading'


class BuildAntButton(Button):
    def __init__(self, ant_type, *args, **kwargs):
        super(BuildAntButton, self).__init__(*args, **kwargs)

        self.ant_type = ant_type
        self.state = STATE_BUTTON
        self.counter = 0
        self._loading_angle = 0

    def draw(self):
        if self.state == STATE_BUTTON:
            self.draw_add_button()
        elif self.state == STATE_LOADING:
            self.draw_loading()

    def draw_counter(self):
        x = self.x - 20
        y = self.y - 20
        rect = [x, y, 40, 40]
        self.view.screen.fill(self.color2, rect)

        largeText = pygame.font.SysFont('centuryschoolbook', 40)
        TextSurf = largeText.render(str(self.counter), True, (56, 56, 56))
        TextRect = TextSurf.get_rect()
        TextRect.center = (self.x, self.y)
        self.view.screen.blit(TextSurf, TextRect)

    def draw_add_button(self):
        rect = [self.x, self.y, self.width, self.height]
        self.view.screen.fill(self.color1, rect, 2)

        largeText = pygame.font.SysFont('centuryschoolbook', 120)
        TextSurf = largeText.render("+", True, (56, 56, 56))
        TextRect = TextSurf.get_rect()
        TextRect.center = (self.x + math.floor(self.width / 2), self.y + math.floor(self.height / 2) - 5)
        self.view.screen.blit(TextSurf, TextRect)

        self.draw_counter()

    def draw_loading(self):
        if self._loading_angle > 360:
            self.state = STATE_BUTTON
            self._loading_angle = 0

        start = (90 - self._loading_angle) / 180 * PI
        end = PI / 2
        rect = [self.x, self.y, self.width, self.height]
        self.view.screen.fill(self.color1, rect, 2)

        arc_width = int(min(self.width, self.height) / 2)

        pygame.draw.arc(self.view.screen, self.color2, rect, start, end, arc_width)
        denominator_angle = all_params.controller_params.framerate * all_params.controller_params.create_ant_time
        self._loading_angle += 360 / denominator_angle

        self.draw_counter()
