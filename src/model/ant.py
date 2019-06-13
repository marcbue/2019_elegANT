import numpy as np
from abc import ABC, abstractmethod

from .game_object import GameObject

from src.utils import randint, array
from src.settings import all_params

distance = np.linalg.norm


class Ant(GameObject, ABC):
    def __init__(self, player, home_nest, foodiness=0, inscentiveness=0, directionism=0, explorativeness=0):
        """Initialize ant object owner and position

        :param player: (Player) Owning Player of the ant
        :param home_nest: (Nest) Coordinates of ant position

        """
        position = home_nest.position.copy()
        super(Ant, self).__init__(position)
        self.owner = player
        # TODO: This is to be done outside of the ant class
        # self.owner.ants.add(self)

        # All ants always have these
        self.energy = all_params.ant_model_params.initial_energy
        self.direction = all_params.ant_model_params.initial_direction
        self.home = home_nest
        self.direction_memory = all_params.ant_model_params.direction_memory

        # Different ant types use a different subset of these parameters. All ants ar instantiated with all present
        # parameters, and the ant type itself decides which ones to use. This mechanism is consists of the fact that
        # the abstract class has setters for all of these values that automatically set these parameters to an invalid
        # value and each Ant type should override only the setters of the variables that it actually uses.
        self.foodiness = foodiness
        self.inscentiveness = inscentiveness
        self.directionism = directionism
        self.explorativeness = explorativeness

    @property
    def foodiness(self):
        return self.__foodiness

    @foodiness.setter
    def foodiness(self, value):
        self.__foodiness = None

    @property
    def inscentiveness(self):
        return self.__inscentiveness

    @inscentiveness.setter
    def inscentiveness(self, value):
        self.__inscentiveness = None

    @property
    def directionism(self):
        return self.__directionism

    @directionism.setter
    def directionism(self, value):
        print("Used superclass setter")
        self.__directionism = None

    @property
    def explorativeness(self):
        return self.__explorativeness

    @explorativeness.setter
    def explorativeness(self, value):
        self.__explorativeness = None

    def __str__(self):
        return ("Ant {} at position {} and energy lvl {} from player {} \n with character variables Foodiness {},  "
                "Inscentiveness {}, Directionism {}, Explorativeness {}").format(self.id, self.position,
                                                                                 self.energy, self.owner,
                                                                                 self.foodiness, self.inscentiveness,
                                                                                 self.directionism,
                                                                                 self.explorativeness)

    def get_position(self):
        """
        Get the coordinates of the object ant position
        :return:
        """
        return self.position

    @abstractmethod
    def update(self, *args):
        if self.energy <= all_params.ant_model_params.min_energy:
            return None, None

    def move_randomly(self):
        """
        changes the position of the ant using a random walk and combining it with the previous direction
        direction is updated
        :return: the updated position is returned
        """
        while True:  # to avoid standing still and divide by zero
            movement = randint(low=-1, high=2, size=2)  # random move
            self.direction += self.direction_memory * self.direction + movement
            if distance(self.direction) > 0.:
                break
        self.direction /= distance(self.direction)
        self.position = self.position + self.direction
        return self.position

    def move_to(self, obj_position):
        """
        changing the position of the ant towards the given obj_position with step size of one
        direction is updated
        :param obj_position: the position of object which the ant should move towards
        :return: the updated position
        """
        # Go towards the position of obj_position
        if distance(obj_position - self.position) > 0.:
            return_movement = (obj_position - self.position) / distance(obj_position - self.position)
        else:
            return_movement = array([0., 0.])  # THIS IS NOT THE BEST IMPLEMENTATION
        self.position += return_movement
        self.direction = return_movement
        return self.position
