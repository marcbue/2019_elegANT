from .dialog_box import DialogBox
import pygame


class DialogBoxAnt(DialogBox):
    def __init__(self, view, identifier, ant):
        super(DialogBoxAnt, self).__init__(view, identifier, x=view.size[0], y=view.size[1]*0.75, width=view.size[0], height=view.size[1]*0.25)
        self.ant = ant

    def draw(self):
        if self.ant.active:
            print(self.rect)
            for i, stat in enumerate(self.ant.stats):
                self.view.screen.blit(f"{stat.key} : {stat.value}", (self.rect.x + 5, self.rect.y + (i+1)*5))
            pygame.draw.rect(self.view.screen, pygame.Color("black"), self.rect, 2)
