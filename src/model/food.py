from .game_object import Game_object

class Food(Game_object):

    def __init__(self, position, size):
        super(Food, self).__init__(position)
        self.size = size
