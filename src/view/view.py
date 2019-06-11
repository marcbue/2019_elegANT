import sys
import pygame
from .text import Text
from .button import Button
from .color_selector import ColorSelector
from .input_box import InputBox
# TODO check if these imports are necessary
# from .nest import Nest
# from .ant import Ant
from .world import World
from src.utils import array
from .dialog_box_nest import DialogBoxNest
from .dialog_box_add_ants import DialogBoxAddAnts
# import numpy as np
import platform

# View
class View:
    STARTVIEW = 'start-view'
    GAMEVIEW = 'game-view'

    def __init__(self, width, height):
        pygame.init()
        display_info = pygame.display.Info()

        # Currently not used
        self.width = width
        self.height = height
        self.res_width = display_info.current_w
        self.res_height = display_info.current_h
        self.state = None

        # Only works for windows --> need to check operating system
        if platform.system() == 'Windows':
            from ctypes import windll
            windll.user32.SetProcessDPIAware()
            true_res = (windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1))
            self.screen = pygame.display.set_mode(true_res, pygame.FULLSCREEN)

        else:
            self.screen = pygame.display.set_mode((self.res_width, self.res_height), pygame.FULLSCREEN)

        self.background_color = pygame.Color("white")
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_event = pygame.mouse.get_pressed()
        self.elements = {}
        self.event_dict = {}
        self.FONT = pygame.font.Font(None, 32)
        self.pos = [array([-500, 500]), array([500, -500])]

    def change_view_state(self, state):
        if self.state == state:
            return
        # Destroy all UI elements that are no longer needed and clear screen
        self.elements = {}
        self.screen.fill(self.background_color)
        # Construct new UI elements for the requested state
        if state == View.STARTVIEW:
            self.state = View.STARTVIEW
            self._start_view()
        if state == View.GAMEVIEW:
            self.state = View.GAMEVIEW
            self._game_view()

    def _start_view(self):
        self.elements = {}

        # add elements for the main text
        text = Text(self, "headline", 17.5, 10, 0.8, 0.9)
        text.set_text("ElegANT")
        self.add_element(text)

        # Add element for choosing players color
        player_colors = [
            (219, 95, 87),
            (219, 194, 87),
            (145, 219, 87),
            (87, 219, 128),
            (87, 211, 219),
            (87, 112, 219),
            (161, 87, 219),
            (219, 87, 178)
        ]

        self.add_element(ColorSelector(self, "color_selector", 60, 50, 20, 20, player_colors))

        start_button = Button(self, "start_button", 5, 85, 12.5, 10, -1, (100, 100, 100), (150, 150, 150), 'square')

        # Add start game event
        start_button.on("click", lambda: self.event_dict.update(
            {
                "start_button": (
                    self.get_element_by_id("color_selector").get_selection(),
                    self.get_element_by_id("textbox").text
                )
            }
        ))

        self.add_element(start_button)

        starttext = Text(self, "starttext", 11.5, 90, 0.5, 0.6)
        starttext.set_text("START")
        self.add_element(starttext)

        quit_button = Button(self, "quit_button", 98.25, 0.8, 1.5, 2.5, -1, (250, 0, 0), (150, 150, 150), 'square')
        self.add_element(quit_button)
        
        quit_button.on("click", lambda: self.event_dict.update({"quit_game": ()}))

        quittext = Text(self, "quittext", 99, 2, 0.3, 0.4)
        quittext.set_text("X")
        self.add_element(quittext)

        inputname = Text(self, "inputname", 13, 27, 0.5, 0.4)
        inputname.set_text("Please enter your name")
        self.add_element(inputname)

        self.add_element(InputBox(self, "textbox", 5, 32, 12.5, 5, (0, 0, 0), (255, 100, 100), ''))

        buttontext = Text(self, "buttontext", 60, 27, 0.5, 0.4)
        buttontext.set_text("Please choose color of ant")
        self.add_element(buttontext)

    def _game_view(self):
        self.elements = {}

        # add quit button
        quit_button = Button(self, "quit_button", 98.25, 0.8, 1.5, 2.5, -1, (250, 0, 0), (150, 150, 150), 'square')
        self.add_element(quit_button)

        quit_button.on("click", lambda: self.event_dict.update({"quit_game": ()}))

        quittext = Text(self, "quittext", 99, 2, 0.3, 0.4)
        quittext.set_text("X")
        self.add_element(quittext)

        # Create world which contains all game objects
        self.add_element(World(self, "world", 0, 0, 250, 250))

        dialog_add_ants = DialogBoxAddAnts(self, "view_box_id_add_ants_box", active=False)
        self.add_element(dialog_add_ants)

        change_scout_stats = Button(self, "change_scout_stats", 0, 0, 10, 10, -1, pygame.Color("white"),
                                    (150, 150, 150), 'square', has_image=True,
                                    image_path="src/view/images/scout_stat_button.png")

        self.add_element(DialogBoxNest(self,
                                       f"view_box_id_scout_box",
                                       slider_data=[
                                           {"name": "Explorativeness", "min_value": 0,
                                            "max_value": 100, "default_value": 50, "identifier": "0000"},
                                           {"name": "Aggressiveness", "min_value": 0,
                                            "max_value": 100, "default_value": 50, "identifier": "0001"}],
                                       active=False,
                                       name="Scout Stats"))

        change_scout_stats.on("click", lambda: self.get_element_by_id("view_box_id_scout_box").toggle())

        self.add_element(change_scout_stats)

    def add_element(self, ui_element):
        self.elements[ui_element.identifier] = ui_element

    def remove_element(self, ui_element_identifier):
        self.elements.pop(ui_element_identifier, None)

    def get_element_by_id(self, identifier):
        if identifier in self.elements:
            return self.elements[identifier]
        else:
            print("Element does not exist")

    def draw(self, model_state=None):
        self.screen.fill(self.background_color)
        iteration_copy = self.elements.copy()
        for element in iteration_copy.values():
            element.draw()
        pygame.display.flip()

    def update(self, game_state):
        if game_state:
            self.elements["world"].update(game_state)
    
    def events(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.event_dict = {}

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                iteration_copy = self.elements.copy()
                for element in iteration_copy.values():
                    element.event_handler(event)

        if self.event_dict:
            print(self.event_dict)

        return self.event_dict

    def increment_ant_count(self, type):
        button = self.get_element_by_id(f"build_{type}")
        button.counter += 1
