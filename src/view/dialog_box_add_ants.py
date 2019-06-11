import math
import pygame
from .dialog_box import DialogBox
from .button_build_ant import BuildAntButton
from .button_ants_dialog import AntsDialogButton


class DialogBoxAddAnts(DialogBox):
    def __init__(self, view, identifier, active=False, name="Dialog_Box"):
        super(DialogBoxAddAnts, self).__init__(view, identifier, x=3, y=87,
                                               width=2, height=10)
        self.active = active
        self.identifier = identifier
        self.name = name
        self.buttons = {}
        self.ant_types = [
           'scout'
        ]
        self.set_buttons()

    def set_buttons(self):
        for index, ant_type in enumerate(self.ant_types):
            build_ant_button = BuildAntButton(
                ant_type,
                self.view,
                f"build_{ant_type}", 15 + (index * 10), 85, 5, 9, -1, (255, 20, 147),
                (255, 105, 180), 'square'
            )

            build_ant_button.on("click", lambda: self.view.event_dict.update({
                f"build_{ant_type}": (build_ant_button.identifier,)
            }))

            self.buttons[build_ant_button.identifier] = build_ant_button

    def toggle(self):
        self.active = not self.active

    def draw(self):
        build_ants_button = AntsDialogButton(self.view, "show_build_ants", 5, 85, 5, 9, -1, (255, 20, 147),
                                             (255, 105, 180), 'square')

        build_ants_button.on("click", lambda: self.view.event_dict.update({
            "show_build_ants": (build_ants_button,)
        }))

        self.view.add_element(build_ants_button)

        if self.active:
            pygame.draw.rect(self.view.screen, pygame.Color("white"), [self.x + 100, self.y - 50, 300, self.height + 50], 2)

            for identifier, button in self.buttons.items():
                self.view.add_element(button)
        else:
            for identifier in self.buttons.keys():
                self.view.remove_element(identifier)
