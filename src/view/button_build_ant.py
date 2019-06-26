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
        self.color_background = (0, 0, 0)
        name = "_".join((str(c) for c in self.color))
        self.image_path = f"src/view/images/{name}_build_worker.png"
        self.image = pygame.image.load(self.image_path)

    def draw(self):
        if self.state == STATE_BUTTON:
            self.draw_add_button()
        elif self.state == STATE_LOADING:
            self.draw_loading()

    def draw_add_button(self):
        super(BuildAntButton, self).draw()
        self.loc = self.image.get_rect().center
        self.loc = (self.x - 10, self.y - 10)
        self.view.screen.blit(self.image, self.loc)
        self.img_width, self.img_height = self.image.get_rect().width, self.image.get_rect().height
        self.draw_counter()
        self.counter_text()

    def draw_loading(self):
        if self._loading_angle > 360:
            self.state = STATE_BUTTON
            self._loading_angle = 0

        self.view.screen.blit(self.image, self.loc)

        self.draw_counter()

        start = (90 - self._loading_angle) / 180 * PI
        end = PI / 2
        rect = [self.loc[0], self.loc[1], self.img_width, self.img_height]
        self.view.screen.fill(self.color_background, rect, 2)
        arc_width = int(self.xradius / 1.5)
        pygame.draw.arc(self.view.screen, self.color2, rect, start, end, arc_width)
        denominator_angle = all_params.controller_params.framerate * all_params.controller_params.create_ant_time
        self._loading_angle += 360 / denominator_angle

        self.counter_text()

    def draw_counter(self):
        self.xcounter = self.x
        self.ycounter = self.y
        self.xradius = int(self.img_width / 5)
        pygame.draw.circle(self.view.screen, self.color, (self.xcounter, self.ycounter), self.xradius)

    def counter_text(self):
        self.fontsize = int(self.xradius) + 10
        largeText = pygame.font.SysFont('Garamond_Bold.ttf', self.fontsize)
        TextSurf = largeText.render(str(self.counter), True, (255, 255, 255))
        TextRect = TextSurf.get_rect()
        TextRect.center = (self.x, self.y)
        self.view.screen.blit(TextSurf, TextRect)





