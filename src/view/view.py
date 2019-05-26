import pygame
from .text import Text
from .button import Button
from .color_selector import ColorSelector
from .input_box import InputBox
from .nest import Nest
from .ant import Ant
from src.utils import array

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
        res_width = display_info.current_w
        res_height = display_info.current_h
        self.res_width = res_width
        self.res_height = res_height
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
        self.pos = [array([0, 0]), array([250, 250])]

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

        # Add elemt for choosing players color
        player_colors = [
            (220, 0, 0),
            (255, 160, 125),
            (0, 0, 255),
            (255, 20, 147),
            (178, 58, 238),
            (0, 245, 255),
            (0, 200, 0),
            (255, 165, 0)
        ]

        self.add_element(ColorSelector(self, "color_selector", 60, 50, 5, 1, player_colors))

        start_button = Button(self, "start_button", 5, 85, 12.5, 10, -1, (100, 100, 100), (150, 150, 150), 'square')

        # Add start game event
        start_button.on("click", lambda: self.event_dict.update({"start_button":
                                                                     (self.get_element_by_id(
                                                                         "color_selector").get_selection(),
                                                                      self.get_element_by_id("textbox").text)}))

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

        # add a nest and an ant
        self.add_element(Nest(self, "nest", 650, 400, 30, (220, 0, 0)))  # red
        self.add_element(Ant(self, "ant", 660, 500, 10, (220, 0, 0)))  # peach

        # add quit button
        quit_button = Button(self, "quit_button", 10, 98, 20, 20, -1, (250, 0, 0), (150, 150, 150), 'square')
        self.add_element(quit_button)

        quit_button.on("click", lambda: self.event_dict.update({"quit_game": ()}))

        quittext = Text(self, "quittext", 99, 1.75, -1, -1, 20)
        quittext.set_text("X")
        self.add_element(quittext)

        # TODO add sliders to the game view
        # self.add_element(
        # Button(self, "start_button", 100, 600, 250, 100, -1, (100, 100, 100), (150, 150, 150), 'square'))  # orange
        # starttext = Text(self, "starttext", 225, 650, -1, -1, 50)
        # starttext.set_text("START")
        # self.add_element(starttext)

        build_scout_button = Button(self, "build_scout", 100, 600, 100, 100, -1, (100, 100, 100),
                                    (150, 150, 150), 'square')

        # Add start game event
        build_scout_button.on("click", lambda: self.event_dict.update({"build_scout": ()}))

        self.add_element(build_scout_button)

    def add_element(self, ui_element):
        self.elements[ui_element.identifier] = ui_element

    def get_element_by_id(self, identifier):
        if identifier in self.elements:
            return self.elements[identifier]
        else:
            print("Element does not exist")

    def draw(self, model_state=None):
        self.screen.fill(self.background_color)
        for element in self.elements.values():
            element.draw()
        pygame.display.flip()

    def update(self, game_state):
        pass

    def events(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.event_dict = {}

        for event in pygame.event.get():
            for element in self.elements.values():
                element.event_handler(event)

        if self.event_dict:
            print(self.event_dict)

        return self.event_dict
