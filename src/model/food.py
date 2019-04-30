from .game_object import GameObject

class Food(GameObject):

    def __init__(self, position, size):
        super(Food, self).__init__(position)
        self.size = size
