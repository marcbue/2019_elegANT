from .game_object import GameObject

class Food(GameObject):

    def __init__(self, position, size):
        super(Food, self).__init__(position)
        self.size = size

    def update(self, *args):
        if self.size <= 0:
            return None
        else:
            return self.position

