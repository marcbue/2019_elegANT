
class ViewElement:
    def __init__(self, view, identifier, x, y, width, height):
        self.identifier = identifier
        self.view = view
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.events = {}

    def draw(self):
        pass

    def event_handler(self, event):
        pass

    def on(self, event, fnct, **kwargs):
        if event not in self.events:
            self.events[event] = []
        self.events[event].append((fnct, kwargs))
