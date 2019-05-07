from .world import World

# Interface with controller
# GameState calls world interface
class GameState:
    def __init__(self, player_list):
        self.players = player_list
        self.world = World()
        # TODO create initial objects on world

    def get_objects_in_region(self, top_left, bottom_right):
        pass

    def update(self):
        self.world.update()

    def create_ants(self, nest_position, amount):
        # TODO check if nest is there and create ants at that nest
        self.world.create_ants(nest_position, amount)
        pass

    def create_nest(self, nest_position, color, size, health):
        self.world.create_nests(nest_position, color, size, health)
        pass

    def create_food(self, position_list, size_list):
        self.world.create_food(position_list, size_list)
        pass


