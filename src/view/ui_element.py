from .view_element import ViewElement
import pygame


class UIElement(ViewElement):

    def __init__(self, view, identifier, x, y, width, height, active=False):
        self.x_percentage = x
        self.y_percentage = y
        self.w_percentage = width
        self.h_percentage = height
        x = 0 + int(x * view.width)
        y = 0 + int(y * view.height)
        width = int(width * view.width)
        height = int(height * view.height)
        super(UIElement, self).__init__(view, identifier, x, y, width, height)

        self.active = active
        self.hovered = False

    def event_handler(self, event):
        pos = self.view.mouse_pos

        if self.mouse_on_object(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if "click" in self.events:
                    for fnct, args in self.events["click"]:
                        fnct(**args)
            
            if self.hovered is False:
                self.hovered = True
                if "enter" in self.events:
                    for fnct, args in self.events["enter"]:
                        fnct(**args)
            
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
                
            if self.hovered is True:
                self.hovered = False
                if "leave" in self.events:
                    for fnct, args in self.events["leave"]:
                        fnct(**args)

        if self.active and event.type == pygame.KEYDOWN:
            if "keyback" in self.events and event.key == pygame.K_BACKSPACE:
                for fnct, args in self.events["keyback"]:
                    fnct(**args)

            elif "keyret" in self.events and event.key == pygame.K_RETURN:
                for fnct, args in self.events["keyret"]:
                    fnct(**args)

            elif "keychar" in self.events:
                for fnct, args in self.events["keychar"]:
                    fnct(event.unicode, **args)

    def mouse_on_object(self, pos):
        if self.shape == 'circle':
            return self.x + self.radius > pos[0] > self.x - self.radius \
                and self.y + self.radius > pos[1] > self.y - self.radius
        elif self.shape == 'square':
            return self.x + self.width > pos[0] > self.x and self.y + self.height > pos[1] > self.y

    def draw(self):
        self.x = 0 + int(self.x_percentage * self.view.width)
        self.y = 0 + int(self.y_percentage * self.view.height)
        self.width = 0 + int(self.w_percentage * self.view.width)
        self.height = 0 + int(self.h_percentage * self.view.height)


