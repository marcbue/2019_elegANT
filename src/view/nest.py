from view_element import ViewElement

class Nest(ViewElement):
    def __init__(self, view, identifier, x, y, radius, color):
        super(Nest, self).__init__(view, identifier, x, y)
        self.color = color
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.view.screen, self.color, (self.x, self.y), self.radius)

    def event_handler(self, event):
        pass

