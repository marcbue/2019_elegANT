import sys
import pygame
from text import Text
from button import Button
from input_box import InputBox
from nest import Nest
from ant import Ant
# import numpy as np

# View
class View:
    STARTVIEW = 'start-view'
    GAMEVIEW = 'game-view'

    def __init__(self, width, height):
        pygame.init()

        self.state = None #View.STARTVIEW
        self.size = width, height
        self.screen = pygame.display.set_mode(self.size)
        self.color = self.screen.fill((247, 247, 247))
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_event = pygame.mouse.get_pressed()
        self.elements = {}
        self.FONT = pygame.font.Font(None, 32)

    def change_view_state(self, state):
        if self.state == state:
            return
        # Destroy all UI elements that are no longer needed
        self.elements = {}
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

        # add element for choosing each color of ant
        self.add_element(Button(self, "red_button", 850, 200, -1, -1, 25, (220, 0, 0), (255, 84, 84)))  # red
        self.add_element(Button(self, "peach_button", 850, 500, -1, -1, 25, (255, 160, 125), (255, 218, 185)))  # peach
        self.add_element(Button(self, "blue_button", 700, 350, -1, -1, 25, (0, 0, 255), (30, 144, 255)))  # blue
        self.add_element(Button(self, "pink_button", 1000, 350, -1, -1, 25, (255, 20, 147), (255, 95, 225)))  # pink
        self.add_element(Button(self, "purple_button", 750, 460, -1, -1, 25, (178, 58, 238), (171, 130, 255)))  # purple
        self.add_element(
            Button(self, "light_green_button", 950, 250, -1, -1, 25, (0, 245, 255), (187, 255, 255)))  # turquoise
        self.add_element(Button(self, "green_button", 750, 250, -1, -1, 25, (0, 200, 0), (0, 255, 0)))  # green
        self.add_element(Button(self, "orange_button", 950, 460, -1, -1, 25, (255, 165, 0), (255, 210, 30)))  # orange

        # add element for starØt button and the text on it
        self.add_element(
            Button(self, "start_button", 100, 600, 250, 100, -1, (100, 100, 100), (150, 150, 150), 'square'))  # orange
        starttext = Text(self, "starttext", 225, 650, -1, -1, 50)
        starttext.set_text("START")
        self.add_element(starttext)

        # add element for the input box name
        self.add_element(InputBox(self, "textbox", 100, 200, 250, 100, (0, 0, 0), (100, 100, 100), ''))

        def add_element(self, ui_element):
            self.elements[ui_element.identifier] = ui_element

    def _game_view(self):
        self.elements = {}

        # add a nest and an ant
        self.add_element(Nest(self, "nest", 650, 400, 30, (220, 0, 0)))  # red
        self.add_element(Ant(self, "ant", 660, 500, 10, (220, 0, 0)))  # peach

        # add sliders to the game view
        # self.add_element(
        # Button(self, "start_button", 100, 600, 250, 100, -1, (100, 100, 100), (150, 150, 150), 'square'))  # orange
        # starttext = Text(self, "starttext", 225, 650, -1, -1, 50)
        # starttext.set_text("START")
        # self.add_element(starttext)

    def add_element(self, ui_element):
        self.elements[ui_element.identifier] = ui_element

    def get_element_by_id(self, identifier):
        if identifier in self.elements:
            return self.elements[identifier]
        else:
            print("Element does not exist")

    def draw(self, model_state=None):
        for element in self.elements.values():
            element.draw()
        pygame.display.flip()

    def events(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_event = pygame.mouse.get_pressed()
        self.mouse_down = pygame.MOUSEBUTTONDOWN
        self.key_keydown = pygame.KEYDOWN
        self.key_return = pygame.K_RETURN
        self.key_back = pygame.K_BACKSPACE

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                for element in self.elements.values():
                    element.event_handler(event)











