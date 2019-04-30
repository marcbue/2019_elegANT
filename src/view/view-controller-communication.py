#!/usr/bin/env python
# coding: utf-8

import sys
import pygame


# import numpy as np

# View
class View:
    def __init__(self, width, height):
        pygame.init()

        self.size = width, height
        self.screen = pygame.display.set_mode(self.size)
        self.color = self.screen.fill((247, 247, 247))
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_event = pygame.mouse.get_pressed()
        self.elements = {}
        self.FONT = pygame.font.Font(None, 32)

    def start_view(self):
        self.elements = {}

        # add elements for the main text
        text = Text(self, "headline", 250, 100, -1, -1, 115)
        text.set_text("ElegANT")
        self.add_element(text)

        # add element for choosing each color of ant
        self.add_element(Button(self, "red_button", 850, 200, -1, -1, 25, (220, 0, 0), (255, 0, 0)))  # red
        self.add_element(Button(self, "peach_button", 850, 500, -1, -1, 25, (250, 128, 114), (255, 140, 105)))  # peach
        self.add_element(Button(self, "blue_button", 700, 350, -1, -1, 25, (0, 0, 205), (0, 0, 255)))  # blue
        self.add_element(Button(self, "pink_button", 1000, 350, -1, -1, 25, (255, 20, 147), (255, 75, 202)))  # pink
        self.add_element(Button(self, "purple_button", 750, 460, -1, -1, 25, (178, 58, 238), (191, 62, 255)))  # purple
        self.add_element(
            Button(self, "light_green_button", 950, 250, -1, -1, 25, (78, 238, 148), (84, 255, 159)))  # light green
        self.add_element(Button(self, "green_button", 750, 250, -1, -1, 25, (0, 200, 0), (0, 255, 0)))  # green
        self.add_element(Button(self, "orange_button", 950, 460, -1, -1, 25, (255, 165, 0), (255, 200, 20)))  # orange

        # add element for start button and the text on it
        self.add_element(
            Button(self, "start_button", 100, 400, 250, 100, -1, (255, 165, 0), (255, 200, 20), 'square'))  # orange
        starttext = Text(self, "starttext", 225, 450, -1, -1, 50)
        starttext.set_text("START")
        self.add_element(starttext)

        # add element for the input box name
        # self.add_element(InputBox(self,"textbox",100,200,250,100,(0,0,0),(100,100,100),''))

    def add_element(self, ui_element):
        self.elements[ui_element.identifier] = ui_element

    def get_element_by_id(self, identifier):
        if identifier in self.elements:
            return self.elements[identifier]
        else:
            print("Element does not exist")

    def draw(self):
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

        # End game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for element in self.elements.values():
            element.event_listener()


class ViewElement:
    def __init__(self, view, identifier, x, y, width, height):
        self.identifier = identifier
        self.view = view
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.events = {}

    def draw(self):
        pass

    def event_listener(self):
        pass

    def on(self, event, fnct, *args):
        if event not in self.events:
            self.events[event] = []
        self.events[event].append((fnct, args))


class Text(ViewElement):
    def __init__(self, view, identifier, x, y, width, height, fontsize):
        pygame.init()
        super(Text, self).__init__(view, identifier, x, y, width, height)
        self.fontsize = fontsize

    def set_text(self, text):
        self.text = text
        largeText = pygame.font.SysFont('centuryschoolbook', self.fontsize)
        self.TextSurf = largeText.render(self.text, True, (56, 56, 56))
        self.TextRect = self.TextSurf.get_rect()
        self.TextRect.center = (self.x, self.y)

    def draw(self):
        self.view.screen.blit(self.TextSurf, self.TextRect)


class UIElement(ViewElement):
    pass


class Button(UIElement):
    def __init__(self, view, identifier, x, y, width, height, radius, color1, color2, shape='circle'):
        super(Button, self).__init__(view, identifier, x, y, width, height)
        self.color1 = color1
        self.color2 = color2
        self.color = color1
        self.radius = radius
        self.shape = shape
        self.width = width
        self.height = height
        self.on("hover", self.change_color, self.color2)
        self.on("leave", self.change_color, self.color1)

    def change_color(self, new_color):
        self.color = new_color

    def draw(self):
        if self.shape == 'circle':
            pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), self.radius)
        elif self.shape == 'square':
            pygame.draw.rect(self.view.screen, self.color, (self.x, self.y, self.width, self.height))
        else:
            print('not valid')

    def event_listener(self):
        pos = self.view.mouse_pos
        event = self.view.mouse_event

        if self.shape == 'circle':
            if self.x + self.radius > pos[0] > self.x - self.radius and self.y + self.radius > pos[1] \
                    > self.y - self.radius:
                if "hover" in self.events:
                    for fnct, args in self.events["hover"]:
                        fnct(args)
                if "click" in self.events and event[0] == 1:
                    for fnct, args in self.events["click"]:
                        fnct(args)
            else:
                if "leave" in self.events:
                    for fnct, args in self.events["leave"]:
                        fnct(args)
        if self.shape == 'square':
            if self.x + self.width > pos[0] > self.x and self.y + self.height > pos[1] > self.y:
                if "hover" in self.events:
                    for fnct, args in self.events["hover"]:
                        fnct(args)
                if "click" in self.events and event[0] == 1:
                    for fnct, args in self.events["click"]:
                        fnct(args)
            else:
                if "leave" in self.events:
                    for fnct, args in self.events["leave"]:
                        fnct(args)


class InputBox(UIElement):

    def __init__(self, view, identifier, x, y, width, height, color1, color2, text=''):
        super(InputBox, self).__init__(view, identifier, x, y, width, height)
        self.rect = pygame.Rect(x, y, width, height)
        self.color1 = color1
        self.color2 = color2
        self.color = color1
        self.text = text
        self.txt_surface = self.view.FONT.render(text, True, self.color)
        self.active = False
        self.on("mouseclick", self.mouse_click, self.color2)
        self.on("keyret", self.keyret, self.text)
        self.on("keyback", self.keyback, self.text)

    def mouse_click(self, newcolor):
        self.active = not self.active
        self.color = newcolor

    def keyret(self, text):
        print(text)
        self.text = ''

    def keyback(self, text):
        self.text = text[:-1]

    def event_listener(self):
        pygame.init()
        pos = self.view.mouse_pos
        # m_down = self.view.mouse_down
        # m_event = self.view.mouse_event
        # k_return = self.view.key_return
        # k_down = self.view.key_keydown
        # k_backspace = self.view.key_back

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pos):
                    if "mouseclick" in self.events:
                        for fnct, args in self.events["mouseclick"]:
                            fnct(args)
                else:
                    self.active = False
            if event.type == pygame.KEYDOWN:
                print('txt loop')
                if self.active:
                    if event.type == pygame.K_RETURN:
                        print('ret loop')
                        if "keyret" in self.events:
                            for fnct, args in self.events["keyret"]:
                                fnct(args)
                    if event.type == pygame.K_BACKSPACE:
                        print('back loop')
                        if "keyback" in self.events:
                            for fnct, args in self.events["keyback"]:
                                fnct(args)
                    else:
                        print('Print text')
                        self.text += event.unicode
                    self.txt_surface = self.view.FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self):
        self.view.screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(self.view.screen, self.color, self.rect, 2)


def greet():
    print('hello')


class Controller:
    def __init__(self):
        self.view = View(1300, 800)
        self.view.start_view()

        # start_message = self.view.get_element_by_id("headline")
        # first_button = self.view.get_element_by_id("start_button")
        # text_button = self.view.get_element_by_id("starttext")

        # start_button.on("click", greet)
        # first_button.on("hover", lambda: print("Hover!"))

        self.game_loop()

    def game_loop(self):
        while True:
            self.view.events()
            self.view.draw()


controller = Controller()
