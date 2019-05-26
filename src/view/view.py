import sys
import pygame
from .text import Text
from .button import Button
from .color_selector import ColorSelector
from .input_box import InputBox
from .nest import Nest
from .ant import Ant
from .world import World
from src.utils import array
from .dialog_box_nest import DialogBoxNest


# import numpy as np

# View
class View:
    STARTVIEW = 'start-view'
    GAMEVIEW = 'game-view'

    def __init__(self, width, height):
        pygame.init()
        self.state = None
        self.size = width, height
        self.screen = pygame.display.set_mode(self.size)
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
        text = Text(self, "headline", 250, 100, -1, -1, 115)
        text.set_text("ElegANT")
        self.add_element(text)

        # Add element for choosing players color
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
        self.add_element(ColorSelector(self, "color_selector", 850, 350, 150, player_colors))

        # add element for start button and the text on it
        start_button = Button(self, "start_button", 100, 600, 250, 100, -1,
                              (100, 100, 100), (150, 150, 150), shape='square')

        # Add start game event
        start_button.on("click", lambda: self.event_dict.update({"start_button":
                                                                     (self.get_element_by_id(
                                                                         "color_selector").get_selection(),
                                                                      self.get_element_by_id("textbox").text)}))

        self.add_element(start_button)

        starttext = Text(self, "starttext", 225, 650, -1, -1, 50)
        starttext.set_text("START")
        self.add_element(starttext)

        inputname = Text(self, "inputname", 220, 250, -1, -1, 30)
        inputname.set_text("Please enter your name")
        self.add_element(inputname)

        # add element for the input box name
        self.add_element(InputBox(self, "textbox", 100, 300, 250, 50, (0, 0, 0), (255, 100, 100), ''))

    def _game_view(self):
        self.elements = {}

        # Create world which contains all game objects
        self.add_element(World(self, "world", 0, 0, 250, 250))

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

        change_scout_stats = Button(self, "change_scout_stats", 0, 0, 100, 100, -1, pygame.Color("white"),
                                    (150, 150, 150), 'square', has_image=True,
                                    image_path="src/view/images/scout_stat_button.png")

        self.add_element(DialogBoxNest(self,
                                       f"view_box_id_scout_box",
                                       slider_data=[
                                           {"name": "explorativeness", "min_value": 0,
                                            "max_value": 100, "default_value": 50, "identifier": "0000"},
                                           {"name": "aggressiveness", "min_value": 0,
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
