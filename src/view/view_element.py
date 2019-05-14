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

    def event_handler(self, event):
        print('event not handled')

    def on(self, event, fnct, **kwargs):
        if event not in self.events:
            self.events[event] = []
        self.events[event].append((fnct, kwargs))
