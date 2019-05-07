from .kd_tree_and_dict import KdTreeAndDict


class GameState:
    def __init__(self, player_list):
        self.players = player_list
        self.world = KdTreeAndDict()
        # TODO create initial objects on world
        all_colors = [player.color for player in player_list]
        # TODO: other positions
        positions = []
        for i in range(len(player_list)):
            positions.append((i * 10, i * 10))
        self.world.create_nests(all_colors, positions)

    def get_objects_in_region(self, top_left, bottom_right):
        pass

    def update(self):
        self.world.update()

    def create_ants(self, position, amount):
        # TODO check if nest is there and create ants at that nest
        pass
