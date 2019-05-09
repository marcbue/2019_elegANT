import pygame
from ui_element import UIElement


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

    def change_color(self, new_color):
        self.color = new_color

    def draw(self):
        if self.shape == 'circle':
            pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), self.radius)
        elif self.shape == 'square':
            pygame.draw.rect(self.view.screen, self.color, (self.x, self.y, self.width, self.height))
        else:
            print('not valid')

    def event_handler(self, event):
        pos = self.view.mouse_pos

        if self.shape == 'circle':
            if self.x + self.radius > pos[0] > self.x - self.radius and self.y + self.radius > pos[1] > \
                    self.y - self.radius:
                # if "hover" in self.events:
                #     for fnct, args in self.events["hover"]:
                #         fnct(**args)
                if "click" in self.events and event.type == pygame.MOUSEBUTTONDOWN:
                    print('click_circle')
                    for fnct, args in self.events["click"]:
                        fnct(**args)
        #     else:
        #         if "leave" in self.events:
        #             for fnct, args in self.events["leave"]:
        #                 fnct(**args)
        if self.shape == 'square':
            if self.x + self.width > pos[0] > self.x and self.y + self.height > pos[1] > self.y:
                # if "hover" in self.events:
                #     for fnct, args in self.events["hover"]:
                #         fnct(**args)
                if "click" in self.events and event.type == pygame.MOUSEBUTTONDOWN:
                    print('click')
                    for fnct, args in self.events["click"]:
                        fnct(**args)
            # else:
            #     if "leave" in self.events:
            #         for fnct, args in self.events["leave"]:
            #             fnct(args)
