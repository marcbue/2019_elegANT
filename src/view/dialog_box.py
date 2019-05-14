from view_element import ViewElement
import pygame

class DialogBox(ViewElement):
    def __init__(self,view,identifier,x,y,width,height,background_color=pygame.Color("grey")):
        super(DialogBox, self).__init__(view, identifier, x, y, width, height)
        self.rect = pygame.Rect(x, y, width, height)
        self.background_color = background_color

    def draw(self):
        pass