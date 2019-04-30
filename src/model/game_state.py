from .world import World

class GameState:
    def __init__(self, player_list):
        self.players = player_list
        self.world = World()
        # TODO create initial objects on world

    def get_objects_in_region(self, top_left, bottom_right):
        pass

    def update(self):
        self.world.update()

    def create_ants(self, position, amount):
        # TODO check if nest is there and create ants at that nest
        pass

