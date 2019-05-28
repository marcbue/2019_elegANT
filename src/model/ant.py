import numpy as np

from .food import Food
from .game_object import GameObject
from src.utils import randint, array


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

    def __init__(self, color, home_nest):
        """Initialize ant object color and position

        :param color: (str) Color of the ant
        :param home_nest: (Nest) Coordinates of ant position

        """
        position = home_nest.position
        super(Ant, self).__init__(position)
        # TODO: assign id
        self.color = color
        self.has_food = False
        self.energy = 100
        self.momentum = array([0., 0.])
        self.home = home_nest

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

    def update(self, *args):
        return self.move(args[0])

    def move(self, visible_objects):
        """ Move the ant to a new position at each time iteration. It moves it randomly in the first milestone.

        :param visible_objects: (list) All the possible neighboring positions the ant can move to
        :return:
        """
        if self.has_food:
            return self.move_to(self.home.position)
        for obj in visible_objects:
            if type(obj) == Food:
                return self.move_to(obj.position)
            # 2. elif it smells, go to smell
        else:
            # if no food, it will move randomly
            return self.move_randomly()

    def move_randomly(self):
        while True:  # to avoid standing still and devide by zero
            movement = randint(low=-1, high=2, size=2)  # random move
            self.momentum += 0.5 * self.momentum + movement
            if np.linalg.norm(self.momentum) > 0:
                break
        self.momentum /= np.linalg.norm(self.momentum)
        self.position = self.position + self.momentum
        return self.position

    def move_to(self, obj_position):
        # Go to the nearest nest.
        # TO DO get nearest nest position
        # assuming that nest_position is the nearest nest position
        if np.linalg.norm(obj_position - self.position) > 0:
            return_movement = (obj_position - self.position) / np.linalg.norm(obj_position - self.position)
        else:
            return_movement = array([0, 0])  # THIS IS NOT THE BEST IMPLEMENTATION
        self.position += return_movement
        return self.position

    def set_trace(self):
        """ Add value for pheromones when the ant finds food.

        :return:
        """
        if self.has_food:
            # Only then it is possible.
            pass

    # TODO: This needs an update function that the world class can call for each ant. -- Unless move is going to
    #  handle food detection, loading, unloading, etc...
