from .dialog_box import DialogBox
import pygame


class DialogBoxAnt(DialogBox):
    def __init__(self, view, identifier, ant):
        super(DialogBoxAnt, self).__init__(view, identifier, x=0.75, y=0,
                                           width=0.25, height=1.00)
        self.ant = ant

    def draw(self):
        super(DialogBoxAnt, self).draw()
        if self.ant.active:
            for i, stat in enumerate(self.ant.stats):
                self.view.screen.blit(f"{stat.key} : {stat.value}", (self.rect.x + 5, self.rect.y + (i + 1) * 5))
            pygame.draw.rect(self.view.screen, pygame.Color("black"), self.rect, 2)
