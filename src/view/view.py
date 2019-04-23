import pygame


class View:
    def __init__(self):
        pygame.init()
        self.view = "start_screen"
        size = width, height = 329, 249
        self.screen = pygame.display.set_mode(size)

    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            else:
                return False

    def draw(self):
        if self.view == "start_screen":
            self.screen.fill((124, 124, 124))
            pygame.display.flip()
