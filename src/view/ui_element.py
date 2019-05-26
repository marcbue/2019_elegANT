from .view_element import ViewElement
import pygame


class UIElement(ViewElement):

    def __init__(self, view, identifier, x, y, width, height, active=False):
        super(UIElement, self).__init__(view, identifier, x, y, width, height)

        self.view = view
        self.identifier = identifier

        display_info = pygame.display.Info()
        res_width = display_info.current_w
        res_height = display_info.current_h

        self.x1 = 0+int(x/100*res_width)
        self.y1 = 0+int(y/100*res_height)
        self.w1 = int(width/100*res_width)
        self.h1 = int(height/100*res_height)

        # self.x = x
        # self.y = y
        # self.width = width
        # self.height = height

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
                self.active = False
                
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
            return self.x1 + self.radius > pos[0] > self.x1 - self.radius \
                and self.y1 + self.radius > pos[1] > self.y1 - self.radius
        elif self.shape == 'square':
            return self.x1 + self.width > pos[0] > self.x1 and self.y1 + self.height > pos[1] > self.y1


