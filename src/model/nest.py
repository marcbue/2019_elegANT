from .game_object import GameObject


class Nest(GameObject):
    def __init__(self, position, color, size=10, health=100):
        super(Nest, self).__init__(position)
        # TODO: also needs id
        self.color = color
        self.size = size
        self.health = health
        self.food = 0
        self.ant_ids = set()

    def increase_food(self, food_amount):
        self.food += food_amount

    def create_ant(self):
        ant_cost = 1
        if self.food >= ant_cost:
            self.food -= ant_cost
            # Generate ant at position in nest.

    def decrease_health(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Oh no, your colony has a problem!")
            # TODO: remove colony

    def get_number_of_ants(self):
        return len(self.ant_ids)
