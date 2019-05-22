from .dialog_box import DialogBox
from .slider import Slider
import pygame


class DialogBoxNest(DialogBox):
    def __init__(self, view, identifier, properties, active="False", name="Dialog_Box"):
        super(DialogBoxNest, self).__init__(view, identifier, x=view.size[0] * 0.75, y=0,
                                            width=view.size[0] * 0.25, height=view.size[1])
        self.properties = properties
        self.active = active
        self.identifier = identifier
        self.sliders = []
        self.set_sliders()
        self.name = name

    def toggle(self):
        self.active = not self.active

    def set_sliders(self):
        for i, (key, value) in enumerate(self.properties.items()):
            self.sliders.append(Slider(self.view, f"slider_{key}", value, self.x + self.width * 0.1,
                                       self.y + 100 * (i + 1), self.width * 0.80, 20, name=key))

    def draw(self):
        if self.active:
            pygame.draw.rect(self.view.screen, pygame.Color("black"), self.rect, 2)
            txt_surface = self.view.FONT.render(self.name, True, pygame.Color("black"))
            self.view.screen.blit(txt_surface, (self.rect.x + 10, self.rect.y + 10))
            for slider in self.sliders:
                self.view.add_element(slider)
        else:
            for slider in self.sliders:
                self.view.remove_element(slider.identifier)
