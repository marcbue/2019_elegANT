from nest import Nest


class Map:

    def __init__(self, x_size, y_size, player):
        self.x_size = x_size
        self.y_size = y_size
        self.color = player.get_color()

        # Keep track of all objects that are on the map.
        self.nests = []
        self.init_nest(position=None)

    def init_nest(self, position=None):
        # TODO: Make (random or probably central) starting position.
        central_position = None
        self.create_nest(central_position)

    def create_nest(self, position):
        nest = Nest(self.color, position)
        self.nests.append(nest)
