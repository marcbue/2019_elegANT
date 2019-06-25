import math

from .ui_element import UIElement
from .button import Button


class ColorSelector(UIElement):
    def __init__(self, view, identifier, x, y, width, height, colors):
        super(ColorSelector, self).__init__(view, identifier, x, y, width, height)
        self.color = None
        self.buttons = []
        self.colors = colors
        self.colors_n = len(self.colors)
        self.currwidth = self.width
        self.flag = False
        self.colorbutton(self.x, self.y, self.width)

    def colorbutton(self, x, y, width):
        self.buttons = []
        self.x = x
        self.y = y
        self.width = width
        self.radius = self.width // 2
        for i, rgb in enumerate(self.colors):
            x = int(self.radius * math.cos(i * ((2 * math.pi) / self.colors_n))) + self.x
            y = int(self.radius * math.sin(i * ((2 * math.pi) / self.colors_n))) + self.y
            name = "_".join((str(c) for c in rgb))
            button = Button(self.view, "c{}".format(i), x, y, -1, -1, 32, (249, 249, 249), rgb,
                            "circle", True, f"src/view/images/menu_color_{name}_inactive.png")
            button.width = button.height = 100
            button.x = x
            button.y = y
            button.on("click", self._select_color, button_clicked=button)
            self.buttons.append(button)
        self._select_color(button)

    def draw(self):
        super(ColorSelector, self).draw()
        if self.currwidth == self.width:
            self.flag = False
        else:
            self.flag = True
        if self.flag:
            self.colorbutton(self.x, self.y, self.width)
            self.currwidth = self.width
            self.flag = False
        for button in self.buttons:
            button.draw(flag=0)

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
