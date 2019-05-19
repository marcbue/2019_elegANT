import numpy as np

from .game_object import GameObject
from src.utils import randint


class Ant(GameObject):
    """
            A class used to represent an ant object
            It inherits from GameObject class

            ...

            Attributes
            ----------
            color: string
                a string of the ant color
            position: list
                a list of the ant coordinates
            has_food: boolean
                a flag that specifies whether the ant has food or not
            energy: int
                a number that specifies current energy value the ant has

    """

    def __init__(self, color, position):
        """Initialize ant object color and position

        :param color: (str) Color of the ant
        :param position: (list) Coordinates of ant position

        """
        super(Ant, self).__init__(position)
        # TODO: assign id
        self.color = color
        self.has_food = False
        self.energy = 100
        self.momentum = np.array([0., 0.], dtype=np.float64)

    def get_position(self):
        """ Get the coordinates of the object ant position

        :return:

        """
        return self.position

    def unload_food(self):  # TO DO
        """ Flip (has_food) variable to false when the ant reaches the nest and unload the food

        :return:
        """
        # if self.position == nest.position():
        #     self.has_food = False
        #     nest.increase_food(1)
        pass

    def load_food(self):
        """ Flip (has_food) variable to true when the ant finds food

        :return:
        """
        self.has_food = True

    def move(self, possible_positions):
        """ Move the ant to a new position at each time iteration. It moves it randomly in the first milestone.

        :param possible_positions: (list) All the possible neighboring positions the ant can move to
        :return:
        """
        position = self.position
        if self.has_food:
            # Go to the nearest nest.
            # TO DO get nearest nest position
            # assuming that nest_position is the nearest nest position
            nest_position = None
            return_movement = (nest_position - position) / np.linalg.norm(nest_position - position)
            position += return_movement

        # 2. elif it smells, go to smell
        else:  # if no food, it will move randomly

            movement = randint(low=-1, high=2, size=2)
            self.momentum += .5 * self.momentum + movement
            self.momentum /= np.linalg.norm(self.momentum)
            position = position + self.momentum
            return position

    def set_trace(self):
        """ Add value for pheromones when the ant finds food.

        :return:
        """
        if self.has_food:
            # Only then it is possible.
            pass

    # TODO: This needs an update function that the world class can call for each ant. -- Unless move is going to
    #  handle food detection, loading, unloading, etc...
