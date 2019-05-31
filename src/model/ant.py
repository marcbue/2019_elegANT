import numpy as np

from .food import Food
from .game_object import GameObject
from src.utils import randint, array
from .pheromone import Pheromone


class Ant(GameObject):
    """
            A class used to represent an ant object
            It inherits from GameObject class

            ...

            Attributes
            ----------
            owner: Player object that the Pheromone belongs to
            position: list
                a list of the ant coordinates
            has_food: fload
                how much food the ant is carrying
            energy: int
                a number that specifies current energy value the ant has

    """

    def __init__(self, player, home_nest):
        """Initialize ant object owner and position

        :param player: (Player) Owning Player of the ant
        :param home_nest: (Nest) Coordinates of ant position

        """
        position = home_nest.position
        super(Ant, self).__init__(position)
        self.owner = player
        self.has_food = 0
        self.energy = 100
        self.direction = array([0., 0.])
        self.home = home_nest
        self.pheromone_strength = 0.

        # setting parameters
        self.loading_capacity = 1.
        self.min_pheromone_strength = 1.
        self.max_pheromone_strength = 10.
        self.pheromone_dist_decay = 0.95
        self.direction_memory = 0.5

    def get_position(self):
        """
        Get the coordinates of the object ant position
        :return:
        """
        return self.position

    def unload_food(self):  # TO DO
        """
        Flip (has_food) variable to 0 when the ant reaches the nest and unload the food
        :return:
        """
        if self.position == self.home.position():
            self.home.increase_food(self.has_food)
            self.has_food = 0

    def load_food(self, food):
        """
        increase (has_food) variable to loading capacity when the ant finds food
        :param food: the food object
        :return:
        """
        if food.size >= self.loading_capacity:
            food.size -= self.loading_capacity
            self.has_food = self.loading_capacity
        else:
            self.has_food = food.size
            food.size = 0

    def update(self, *args):
        if self.has_food:
            return self.move(args[0]), self.set_trace(args[0])
        else:
            if self.at_food(args[0]):
                return self.position, None
            else:
                return self.move(args[0]), None

    def at_food(self, visible_objects):
        """
        checks if ant is at food location, if True, Load Food and set has_food to True
        :param visible_objects:
        :return: True if ant is at food position, else False
        """
        for obj in visible_objects:
            if isinstance(obj, Food):
                if np.isclose(np.round(self.position), np.round(obj.position)).all():
                    self.load_food(obj)
                    self.pheromone_strength = min(100 * (obj.size / np.linalg.norm(self.position - self.home.position)),
                                                  self.max_pheromone_strength) / self.pheromone_dist_decay
                    return True
        else:
            return False

    def move(self, visible_objects):
        """
        Move the ant to a new position at each time iteration. It moves it randomly in the first milestone.
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
        """
        changes the position of the ant using a random walk and combining it with the direction
        :return: the updated position is returned
        """
        while True:  # to avoid standing still and devide by zero
            movement = randint(low=-1, high=2, size=2)  # random move
            self.direction += self.direction_memory * self.direction + movement
            if np.linalg.norm(self.direction) > 0:
                break
        self.direction /= np.linalg.norm(self.direction)
        self.position = self.position + self.direction
        return self.position

    def move_to(self, obj_position):
        """
        changing the position of the ant towards the given obj_position with step size of one
        :param obj_position: the position of object which the ant should move towards
        :return: the updated position
        """
        # Go to the nearest nest.
        # TO DO get nearest nest position
        # assuming that nest_position is the nearest nest position
        if np.linalg.norm(obj_position - self.position) > 0:
            return_movement = (obj_position - self.position) / np.linalg.norm(obj_position - self.position)
        else:
            return_movement = array([0, 0])  # THIS IS NOT THE BEST IMPLEMENTATION
        self.position += return_movement
        return self.position

    def set_trace(self, visible_objects):
        """
        if there is an existing pheromone in the position, add strength
        otherwise it will create a new pheromone
        :param visible_objects:
        :return: None if existing pheromone otherwise a new pheromone object
        """
        self.pheromone_strength = max(self.min_pheromone_strength,
                                      self.pheromone_dist_decay * self.pheromone_strength)
        for obj in visible_objects:
            if isinstance(obj, Pheromone):
                if np.isclose(np.round(self.position), np.round(obj.position)).all():
                    obj.increase(added_strength=self.pheromone_strength)
                    return None
        else:
            return Pheromone(self.position, self.owner, initial_strength=self.pheromone_strength)

    # TODO: This needs an update function that the world class can call for each ant. -- Unless move is going to
    #  handle food detection, loading, unloading, etc...
