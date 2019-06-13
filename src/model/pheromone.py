from .game_object import GameObject
from src.settings import all_params

class Pheromone(GameObject):
    """
            A class used to represent a nest object
            It inherits from GameObject class

            ...

            Attributes
            ----------
            position: ndarray
            color: tuple of ints
                tuple containing the (R,G,B) values
            strength: float
                a number that specifies the pheromone level at this position
    """

    def __init__(self, position, player, initial_strength=all_params.pheromone_model_params.initial_strength):
        """

        :param position: (list) coordinates of the nest
        :param color: (tuple) (R,G,B) color code for the pheromone
        :param inital_strength: inital strength value, decays afterwards
        """
        super(Pheromone, self).__init__(position)
        self.owner = player
        self.strength = initial_strength

    def __str__(self):
        return "Pheromone {} at position {} with strength {} from player {}".format(self.id, self.position,
                                                                                    self.strength, self.owner)

    def update(self, *args):
        self._decay()
        # TODO: use another cutoff value for pheromone disappearance
        if self.strength <= all_params.pheromone_model_params.min_strength:
            self.strength = 0.
            return None
        else:
            return self.position

    def increase(self, added_strength=all_params.pheromone_model_params.added_strength):
        if added_strength <= 0:
            raise ValueError('This function should not be used to decrease pheromone strength (or leave it unchanged)')
        self.strength += added_strength

    def _decay(self):
        # TODO decide on another decaying scheme
        self.strength = all_params.pheromone_model_params.decay_factor * self.strength
