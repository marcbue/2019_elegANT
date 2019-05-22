from .view_element import ViewElement
import pygame

class World(ViewElement):
    
    def event_handler(self, event):
        pos = self.view.mouse_pos
        if event.type == pygame.KEYDOWN:
            if event.key == 273: # up
                print("up")
            if event.key == 275: # right
                print("right")
            if event.key == 274: # down
                print("down")
            if event.key == 276: # left
                print("left")
    
    def draw(self):
        pass
