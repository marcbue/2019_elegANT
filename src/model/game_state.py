from .kd_tree_and_dict import KdTreeAndDict


class GameState:

    """
            A class used to communicate with the model

            ...

            Attributes
            ----------
            player_list : list
                a list of players id that are currently in the game
            world: list
                a list of all game objects and their positions

            Methods
            -------
            get_objects_in_region(top_left, bottom_right):
                Return positions of objects in specific area

            update()
                Return states and positions of all objects a each time iteration

            create_ants(position, amount)
                Return new ant objects

    """

    def __init__(self, player_list):
        """ Initialize player list and create nests for all the players

        Keyword arguments:
        player_list -- list that contains current players IDs

        """
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
        """Return list of positions and all included objects (ants, nests, foods, pheromones, etc) in a specific
                   rectangular area

        Keyword arguments:
        top_left -- list of coordinates of top left point of the rectangle
        bottom_right --  list of coordinates of bottom right point of the rectangle

        """
        pass

    def update(self):
        """Return the states of all the objects and their positions at each time iteration """
        self.world.update()

    def create_ants(self, position, amount):
        """Return new ant objects in the nest with the given positions

        Keyword arguments:
        position -- list of ant position
        amount -- (int) number of ants that should be created

        """
        # TODO check if nest is there and create ants at that nest
        pass
