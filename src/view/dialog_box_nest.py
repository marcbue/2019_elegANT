from .dialog_box import DialogBox
from .slider import Slider
import pygame


class DialogBoxNest(DialogBox):
    def __init__(self, view, identifier, slider_data=[], active=False, name="Dialog_Box"):
        super(DialogBoxNest, self).__init__(view, identifier, x=0.75, y=0,
                                            width=0.25, height=1.00)
        self.slider_data = slider_data
        self.active = active
        self.show_sliders = active
        self.identifier = identifier
        self.sliders = []
        self.set_sliders()
        self.name = name

    def toggle(self):
        self.active = not self.active
        self.show_sliders = self.active
        if self.show_sliders is True:
            for slider in self.sliders:
                self.view.add_element(slider)

    def set_sliders(self):
        for i, data in enumerate(self.slider_data):
            self.sliders.append(Slider(self.view, data["identifier"], self.x_percentage + self.w_percentage * 0.1,
                                       self.y_percentage + self.h_percentage * 0.1 * (i + 1), self.w_percentage * 0.80,
                                       height=self.h_percentage * 0.1, max_value=data["max_value"],
                                       min_value=data["min_value"], default_value=data["default_value"],
                                       name=data["name"]))

    def draw(self):
        super(DialogBoxNest, self).draw()
        if self.active:
            pygame.draw.rect(self.view.screen, pygame.Color("black"), self.rect, 2)
            txt_surface = self.view.FONT.render(self.name, True, pygame.Color("black"))
            self.view.screen.blit(txt_surface, (self.rect.x + 10, self.rect.y + 10))
        else:
            if self.show_sliders is False:
                for slider in self.sliders:
                    self.view.remove_element(slider.identifier)
