import sys
import pygame
# import numpy as np

# View
class View:
    STARTVIEW = '_start-view'
    GAMEVIEW = 'game-view'

    def __init__(self, width, height):
        pygame.init()

        self.state = View.STARTVIEW
        self.size = width, height
        self.screen = pygame.display.set_mode(self.size)
        self.color = self.screen.fill((247, 247 ,247))
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_event = pygame.mouse.get_pressed()
        self.elements = {}
        self.FONT = pygame.font.Font(None, 32)

    def change_view_state(self, state):
        if self.state == state:
            # return
            self.state = state
        # Destroy all UI elements that are no longer needed
        self.elements = {}
        # Construct new UI elements for the requested state
        if self.state == View.STARTVIEW:
            self._start_view()
        if self.state == View.GAMEVIEW:
            self._game_view()


    def _start_view(self):
        self.elements = {}

        # add elements for the main text
        text = Text(self, "headline", 250, 100, -1, -1, 115)
        text.set_text("ElegANT")
        self.add_element(text)

        # add element for choosing each color of ant
        self.add_element(Button(self ,"red_button" ,850 ,200 ,-1 ,-1, 25 ,(220 ,0 ,0) ,(255 ,84 ,84)))  # red
        self.add_element(Button(self ,"peach_button" ,850 ,500 ,-1 ,-1, 25 ,(255 ,160 ,125) ,(255 ,218 ,185)))  # peach
        self.add_element(Button(self ,"blue_button" ,700 ,350 ,-1 ,-1, 25 ,(0 ,0 ,255) ,(30 ,144 ,255)))  # blue
        self.add_element(Button(self ,"pink_button" ,1000 ,350 ,-1 ,-1, 25 ,(255 ,20 ,147) ,(255 ,95 ,225)))  # pink
        self.add_element(Button(self ,"purple_button" ,750 ,460 ,-1 ,-1, 25 ,(178 ,58 ,238) ,(171 ,130 ,255)))  # purple
        self.add_element \
            (Button(self ,"light_green_button" ,950 ,250 ,-1 ,-1, 25 ,(0 ,245 ,255) ,(187 ,255 ,255)))  # turquoise
        self.add_element(Button(self ,"green_button" ,750 ,250 ,-1 ,-1, 25 ,(0 ,200 ,0) ,(0 ,255 ,0)))  # green
        self.add_element(Button(self ,"orange_button" ,950 ,460 ,-1 ,-1, 25 ,(255 ,165 ,0) ,(255 ,210 ,30)))  # orange

        # add element for start button and the text on it
        self.add_element \
            (Button(self ,"start_button" ,100 ,600 ,250 ,100 ,-1 ,(100, 100, 100) ,(150 ,150 ,150) ,'square'))  # orange
        starttext = Text(self, "starttext", 225, 650, -1, -1, 50)
        starttext.set_text("START")
        self.add_element(starttext)

        # add element for the input box name
        self.add_element(InputBox(self ,"textbox" ,100 ,200 ,250 ,100 ,(0 ,0 ,0) ,(100 ,100 ,100) ,''))

        def add_element(self, ui_element):
            self.elements[ui_element.identifier] = ui_element


    def _game_view(self):
        self.elements = {}

        # add a nest and an ant
        self.add_element(Nest(self, "nest", 650, 400, 30, (220, 0, 0)))  # red
        self.add_element(Ant(self, "ant", 660, 500, 10, (220, 0, 0)))  # peach

        # add sliders to the game view
        # self.add_element(
        #     Button(self, "start_button", 100, 600, 250, 100, -1, (100, 100, 100), (150, 150, 150), 'square'))  # orange
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

    def event_handler(self, event):
        print('event not handled')
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


    def set_text(self ,text):
        self.text = text
        largeText = pygame.font.SysFont('centuryschoolbook' ,self.fontsize)
        self.TextSurf = largeText.render(self.text, True, (56 ,56 ,56))
        self.TextRect = self.TextSurf.get_rect()
        self.TextRect.center = (self.x ,self.y)

    def draw(self):
        self.view.screen.blit(self.TextSurf, self.TextRect)

    def event_handler(self, event):
        pass


class UIElement(ViewElement):
    pass


class Button(UIElement):
    def __init__(self, view, identifier, x, y, width, height, radius, color1, color2 ,shape='circle'):
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
        self.on('click', lambda x: None)


    def change_color(self, new_color):
        self.color = new_color

    def draw(self):
        if self.shape == 'circle':
            pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), self.radius)
        elif self.shape == 'square':
            pygame.draw.rect(self.view.screen, self.color, (self.x, self.y ,self.width ,self.height))
        else:
            print('not valid')


    def event_handler(self, event):
        pos = self.view.mouse_pos

        if self.shape == 'circle':
            if self. x +self.radius > pos[0] > self. x -self.radius and self. y +self.radius > pos[1] > \
                    self. y -self.radius:
                # if "hover" in self.events:
                #     for fnct, args in self.events["hover"]:
                #         fnct(args)
                if "click" in self.events and event.type == pygame.MOUSEBUTTONDOWN:
                    print('click_circle')
                    for fnct, args in self.events["click"]:
                        fnct(args)
        #     else:
        #         if "leave" in self.events:
        #             for fnct, args in self.events["leave"]:
        #                 fnct(args)
        if self.shape == 'square':
            if self. x +self.width > pos[0] > self.x and self. y +self.height > pos[1] > self.y:
                # if "hover" in self.events:
                #     for fnct, args in self.events["hover"]:
                #         fnct(args)
                if "click" in self.events and event.type == pygame.MOUSEBUTTONDOWN:
                    print('click')
                    for fnct, args in self.events["click"]:
                        fnct(args)
            # else:
            #     if "leave" in self.events:
            #         for fnct, args in self.events["leave"]:
            #             fnct(args)


class InputBox(UIElement):

    def __init__(self, view, identifier, x, y, width, height, color1, color2 ,text=''):
        super(InputBox, self).__init__(view, identifier, x, y, width, height)
        self.rect = pygame.Rect(x, y, width, height)
        self.color1 = color1
        self.color2 = color2
        self.color = color1
        self.text = text
        self.txt_surface = self.view.FONT.render(text, True, self.color)
        self.active = False
        self.on("mouseclick" ,self.mouse_click ,self.color2)
        self.on("keyret" ,self.keyret ,self.text)
        self.on("keyback" ,self.keyback ,self.text)

    def mouse_click(self ,newcolor):
        self.active = not self.active
        self.color = newcolor

    def keyret(self ,text):
        print(text)
        self.text = ''

    def keyback(self ,text):
        self.text = text[:-1]

    def event_handler(self, event):
        pygame.init()
        pos = self.view.mouse_pos
        m_down = self.view.mouse_down
        m_event = self.view.mouse_event
        # k_return = self.view.key_return
        # k_down = self.view.key_keydown
        # k_backspace = self.view.key_back

        # for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pos):
                if "mouseclick" in self.events:
                    for fnct, args in self.events["mouseclick"]:
                        fnct(args)
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    print('back loop')
                    # if "keyret" in self.events:
                    #     for fnct, args in self.events["keyret"]:
                    #         fnct(args)
                if event.key == pygame.K_RETURN:
                    print('ret loop')
                    # if "keyback" in self.events:
                    #     for fnct, args in self.events["keyback"]:
                    #         fnct(args)
                else:
                    # print('Print text')
                    self.text += event.unicode
                self.txt_surface = self.view.FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width( ) +10)
        self.rect.w = width

    def draw(self):
        self.view.screen.blit(self.txt_surface, (self.rect. x +5, self.rect. y +5))
        pygame.draw.rect(self.view.screen, self.color, self.rect, 2)

class Nest(ViewElement):
    def __init__(self, view, identifier, x, y, radius, color):
        super(Nest, self).__init__(view, identifier, x, y)
        self.color = color
        self.radius = radius
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), self.radius)

    def event_handler(self, event):
        pass

class Ant(ViewElement):
    def __init__(self, view, identifier, x, y, radius, color):
        super(Ant, self).__init__(view, identifier, x, y)
        self.color = color
        self.radius = radius
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), self.radius)

    def event_handler(self, event):
        pass

# class Slider(UIElement):
#     def __init__(self, name, val, maxi, mini, pos):
#         self.val = val  # start value
#         self.maxi = maxi  # maximum at slider position right
#         self.mini = mini  # minimum at slider position left
#         self.xpos = pos  # x-location on screen
#         self.ypos = 550
#         self.surf = pygame.surface.Surface((100, 50))
#         self.hit = False  # the hit attribute indicates slider movement due to mouse interaction
#
#         # Static graphics - slider background #
#         self.surf.fill((100, 100, 100))
#         pygame.draw.rect(self.surf, GREY, [0, 0, 100, 50], 3)
#         pygame.draw.rect(self.surf, ORANGE, [10, 10, 80, 10], 0)
#         pygame.draw.rect(self.surf, WHITE, [10, 30, 80, 5], 0)
#
#     def draw(self):
#
#         # static
#         surf = self.surf.copy()
#
#     # screen
#     screen.blit(surf, (self.xpos, self.ypos))


# Expected usage of View class by Controller class

class Controller:
    def __init__(self):

        self.view = View(1300, 800)
        self.view.change_view_state(View.GAMEVIEW)

        # start_message = self.view.get_element_by_id("headline")
        # first_button = self.view.get_element_by_id("start_button")
        # text_button = self.view.get_element_by_id("starttext")


        # start_button.on("click", greet)
        # first_button.on("hover", lambda: print("Hover!"))

        # self.game_loop()


    def game_loop(self):
        while True:
            self.view.events()
            self.view.draw()

controller = Controller()
controller.game_loop()