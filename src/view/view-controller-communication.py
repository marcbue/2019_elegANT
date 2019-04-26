#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import pygame
import numpy as np


# In[ ]:


# View
class View:
    def __init__(self, width, height):
        pygame.init()
        self.size = width, height
        self.screen = pygame.display.set_mode(self.size)
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_event = pygame.mouse.get_pressed()
        self.elements = {}
    
    def start_view(self):
        self.elements = {}
        #self.add_element(Button(self, "start_button", 0, 10, 100, 200))
        text = Text(self, "headline", 500, 200, -1, -1, 115)
        text.set_text("ElegANT")
        self.add_element(text)
        self.add_element(Button(self,"button1",850,200,-1,-1, 25,(200,0,0),(255,0,0))) #red
        self.add_element(Button(self,"button2",850,500,-1,-1, 25,(200,200,0),(255,255,0))) #yellow
        self.add_element(Button(self,"button3",700,350,-1,-1, 25,(0,0,205),(0,0,255))) #blue
        self.add_element(Button(self,"button4",1000,350,-1,-1, 25,(255,20,147),(255,75,202))) #pink
        self.add_element(Button(self,"button5",750,460,-1,-1, 25,(178,58,238),(191,62,255))) #purple
        self.add_element(Button(self,"button6",950,250,-1,-1, 25,(78,238,148),(84,255,159))) #light green
        self.add_element(Button(self,"button7",750,250,-1,-1, 25,(0,200,0),(0,255,0))) #green
        self.add_element(Button(self,"button8",950,460,-1,-1, 25,(255,165,0),(255,200,20))) #orange
                
        
    
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
        
        # End game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
        
    
    def set_text(self,text):
        self.text = text
        largeText = pygame.font.SysFont('centuryschoolbook',self.fontsize)
        self.TextSurf = largeText.render(self.text, True, (56,56,56))
        self.TextRect = self.TextSurf.get_rect()
        self.TextRect.center = (self.x,self.y)

    def draw(self):
        self.view.screen.blit(self.TextSurf, self.TextRect)
    

class UIElement(ViewElement):
    pass


class Button(UIElement):
    def __init__(self, view, identifier, x, y, width, height, radius, color1, color2,):
        super(Button, self).__init__(view, identifier, x, y, width, height)
        self.color1 = color1
        self.color2 = color2
        self.color = color1
        self.radius = radius
        self.on("hover", self.change_color, self.color2)
        self.on("leave", self.change_color, self.color1)
    
    def change_color(self, new_color):
        self.color = new_color
        
    def draw(self):
        #pygame.draw.rect(self.view.screen, (20, 20, 20), (self.x, self.y, self.w, self.h))
        pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), self.radius)

    def event_listener(self):
        pos = self.view.mouse_pos
        event = self.view.mouse_event
        
        if self.x+self.radius > pos[0] > self.x-self.radius and self.y+self.radius > pos[1] > self.y-self.radius:
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
        #self.color = self.color1


# In[ ]:


def greet():
    print('hello')

class Controller:
    def __init__(self):
        self.view = View(1300, 800)
        self.view.start_view()
        
        
        start_message = self.view.get_element_by_id("headline")
        first_button = self.view.get_element_by_id("button1")
        
        #start_button.on("click", greet)
        #first_button.on("hover", lambda: print("Hover!"))
        
        self.game_loop()
        
    
    def game_loop(self):
        while True:
            self.view.draw()
            self.view.events()

controller = Controller()


# In[ ]:




