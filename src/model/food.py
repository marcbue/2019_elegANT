from .game_object import GameObject
from src.settings import all_params

class Food(GameObject):

    def __init__(self, position, size):
        super(Food, self).__init__(position)
        self.size = size

    def update(self, *args):
        if self.size <= all_params.model_params.food_min_size:
            return None
        else:
            return self.position

    def __str__(self):
        return "Food {} at {} with size {}".format(self.id, self.position, self.size)

    def take_some(self, max_amount):
        actual_amount = min(self.size, max_amount)
        self.size -= actual_amount
        return actual_amount
