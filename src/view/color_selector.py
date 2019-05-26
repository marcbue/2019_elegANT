import math

from .ui_element import UIElement
from .button import Button


class ColorSelector(UIElement):
    def __init__(self, view, identifier, x, y, width, height, colors):
        super(ColorSelector, self).__init__(view, identifier, x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius = int((self.height ** 2 + self.width ** 2) / 2 * self.height)
        print(self.radius)
        self.color = None
        self.buttons = []
        colors_n = len(colors)
        for i, rgb in enumerate(colors):
            rgb_dark = tuple(int(c * (1 / 2.5)) for c in rgb)
            x = int(self.radius * math.cos(i * ((2 * math.pi) / colors_n))) + self.x
            y = int(self.radius * math.sin(i * ((2 * math.pi) / colors_n))) + self.y
            button = Button(self.view, "c{}".format(i), x, y, -1, -1, 25, rgb, rgb_dark, "circle")
            button.on("click", self._select_color, button_clicked=button)
            self.buttons.append(button)
        self._select_color(button)

    def draw(self):
        for button in self.buttons:
            button.draw()

    def event_handler(self, event):
        for button in self.buttons:
            button.event_handler(event)

    def get_selection(self):
        return self.color

    def _select_color(self, button_clicked):
        self.color = button_clicked.color1
        for button in self.buttons:
            button.change_color(button.color2)
        button_clicked.change_color(button_clicked.color1)
