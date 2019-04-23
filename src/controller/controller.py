import sys
from model.model import Player
from view.view import View

class Controller:
    def __init__(self):
        self.player = Player()
        self.view = View()
        self.run()
    
    def run(self):
        while True:
            event = self.view.get_event()
            if event == "quit":
                sys.exit()
            
            self.view.draw()
