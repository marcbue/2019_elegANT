from .game_object import GameObject


class Ant(GameObject):
    def __init__(self, player, position):
        super(Ant, self).__init__(position)
        # TODO: assign id
        self.color = player.get_color()
        self.has_food = False
        self.energy = 100

    def get_position(self):
        return self.position

    def unload_food(self):
        self.has_food = False

    def load_food(self):
        self.has_food = True

    def move(self, possible_positions):
        if self.has_food:
            # Go to the nearest nest.
            pass

        # 2. elif it smells, go to smell
        # 3. move randomly

    def set_trace(self):
        if self.has_food:
            # Only then it is possible.
            pass
