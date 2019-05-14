from dialog_box import DialogBox
import pygame

class DialogBoxAnt(DialogBox):
    def __init__(self,view,identifier,ant):
        super(self, DialogBoxAnt).__init__(self, view, identifier, x=view.size[0], y=view.size[1]*0.75, width=view.size[0], height=view.size[1]*0.25)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.ant = ant

    def draw(self):
        if self.ant.active:
            for i,stat in enumerate(self.ant.stats):
                self.view.screen.blit(f"{stat.key} : {stat.value}", (self.rect.x + 5, self.rect.y + i*5))
            pygame.draw.rect(self.view.screen, self.background_color, self.rect, 2)
