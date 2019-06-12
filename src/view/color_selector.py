import math

from .ui_element import UIElement
from .button import Button


class ColorSelector(UIElement):
    def __init__(self, view, identifier, x, y, width, height, colors):
        super(ColorSelector, self).__init__(view, identifier, x, y, width, height)
        self.radius = self.width // 2
        self.color = None
        self.buttons = []
        colors_n = len(colors)
        for i, rgb in enumerate(colors):
            x = int(self.radius * math.cos(i * ((2 * math.pi) / colors_n))) + self.x
            y = int(self.radius * math.sin(i * ((2 * math.pi) / colors_n))) + self.y
            name = "_".join((str(c) for c in rgb))
            button = Button(self.view, "c{}".format(i), x, y, -1, -1, 32, (249, 249, 249), rgb,
                            "circle", True, f"src/view/images/menu_color_{name}_inactive.png")
            button.height = button.width = 100
            button.x = x
            button.y = y
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
        self.color = button_clicked.color2
        for button in self.buttons:
            name = "_".join((str(c) for c in button.color2))
            button.image_path = f"src/view/images/menu_color_{name}_inactive.png"
        name = "_".join((str(c) for c in button_clicked.color2))
        button_clicked.image_path = f"src/view/images/menu_color_{name}_active.png"
