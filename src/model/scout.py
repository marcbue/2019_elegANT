import numpy as np
import time

from .food import Food
from .ant import Ant
from .pheromone import Pheromone

from src.utils import get_objects_of_type, zeros
from src.settings import all_params

distance = np.linalg.norm


class Scout(Ant):
    """
            A class used to represent an ant object
            It inherits from GameObject class

            ...

            Attributes
            ----------
            player: Player
                Player object that the ant belongs to
            position: list
                a list of the ant coordinates
            found_food: float
                how much food the ant is carrying
            energy: int
                a number that specifies current energy value the ant has
            direction: array
                an array with the orientation/direction of the ant
            home: Nest
                Nest object that the ant belongs to
            pheromone_strength: float
                strength of the pheromone to leave in next step. This depends on food size and distance to nest.
            loading_capacity: float
                maximum amount of food that the ant can carry
            min_pheromone_strength: float
                minimum amount of pheromone that the ant leaves
            max_pheromone_strength: float
                maximum amount of pheromone that the ant leaves
            pheromone_dist_decay: float
                factor by which the pheromone strength is preserved while leaving the trail towards the nest
            direction_memory: float
                used for random movement. how much the ant takes into account the previous direction for new movement
            foodiness: float
                movement preference for big size of food
            inscentiveness: float
                movement preference for high intensity of pheromone
            directionism: float
                movement preference for previous movement direction
            explorativeness: float
                movement preference for big distances from nest

    """

    def __init__(self, player, home_nest, energy=500.,
                 foodiness=1, inscentiveness=0., directionism=1, explorativeness=1, speed=8., loading_capacity=1.,
                 pheromone_strength=1.):
        """Initialize ant object owner, position, and ant type-specific parameters

        :param player: (Player) Owning Player of the ant
        :param home_nest: (Nest) Coordinates of ant position

        """
        super(Scout, self).__init__(player, home_nest, energy,
                                    foodiness, inscentiveness, directionism, explorativeness, speed, loading_capacity,
                                    pheromone_strength)

        self.found_food = 0.  # TODO change to False when VIEW IS READY
        self.owner = player
        self.home = home_nest
        # self.pheromone_strength = all_params.ant_model_params.initial_pheromone_strength

        # setting parameters
        # self.loading_capacity = all_params.ant_model_params.loading_capacity
        self.min_pheromone_strength = all_params.ant_model_params.min_pheromone_strength
        self.max_pheromone_strength = all_params.ant_model_params.max_pheromone_strength
        self.pheromone_dist_decay = all_params.ant_model_params.pheromone_dist_decay

    # TODO: Please decide which type of ant is going to use which of these parameters and make 100% sure to remove the
    #  methods related to unused ones
    #  ^^ Adu: But is this necessary? Won't all unused methods just be returned as None?

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        self.__energy = value

    @property
    def foodiness(self):
        return self.__foodiness

    @foodiness.setter
    def foodiness(self, value):
        self.__foodiness = value

    @property
    def directionism(self):
        return self.__directionism

    @directionism.setter
    def directionism(self, value):
        self.__directionism = value

    @property
    def inscentiveness(self):
        return self.__inscentiveness

    @inscentiveness.setter
    def inscentiveness(self, value):
        self.__inscentiveness = value

    @property
    def explorativeness(self):
        return self.__explorativeness

    @explorativeness.setter
    def explorativeness(self, value):
        self.__explorativeness = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def loading_capacity(self):
        return self.__loading_capacity

    @loading_capacity.setter
    def loading_capacity(self, value):
        self.__loading_capacity = value

    @property
    def pheromone_strength(self):
        return self.__pheromone_strength

    @pheromone_strength.setter
    def pheromone_strength(self, value):
        self.__pheromone_strength = value

    def get_position(self):
        """
        Get the coordinates of the object ant position
        :return:
        """
        return self.position

    def increase_energy(self):
        return super().increase_energy()

    def update(self, *args):
        """
        update logic in order:
            1- if the ant has no more energy left -> remove ant
            2- if the ant has food:
                2.1- check if ant is at nest vicinity -> unload food
                2.2- if ant is not at nest vicinity -> move towards nest
            3- if ant does not have food, should look for food:
                3.1- if there is food in vicinity, load food (calls at_food)
                3.2- else, look for foods and pheromone in noticeable objects based on move() function
        :param args: [iterable?] list/tuple of noticeable objects
        :return: [tuple] updated ant position, new pheromone or None
        """
        super().update()

        if self.found_food:
            # print("found food")
            if self.at_nest():
                # print("at nest")
                return self.position, None
            else:  # Go to nest if ant found food
                # print("go to nest")
                return self.move_to(self.home.position), self.set_trace(args[0])
        else:
            if self.at_food(args[0]):
                # print("at food")
                return self.position, None
            else:
                # print("just move")
                return self.move(args[0]), None

    def move(self, noticeable_objects):
        """
        Move the ant to a new position at each time iteration.
        If food is detected, movement is done in that direction. If no food is detected, pheromones are followed.
        Movement is random if there are no objects in visible objects.
        :param noticeable_objects: (list) All the possible objects that the ant can perceive
        :return: (array) Position to which the ant moves
        """

        # TODO, scouts can follow enemies too
        # TODO: implement move_to_pheromone method

        # getting list of foods from noticeable objects
        foods = get_objects_of_type(noticeable_objects, Food)
        # pheromones = get_objects_of_type(noticeable_objects, Pheromone)

        # Priority is to find food
        if foods:
            return self.move_to_food(foods)

        # In case there is no food, pheromones are taken into account
        # elif pheromones:
        #     return self.move_to_pheromone(pheromones)

        # In case there is no food nor pheromone scents, move randomly
        else:
            return self.move_randomly()

    def at_nest(self):
        """
        checks if ant is close enough to nest position, if True, unload food, and set pheromone strength to zero
        :return: True is ant is at nest position, otherwise False
        """
        at_nest = False

        if distance(self.position - self.home.position) <= all_params.ant_model_params.min_dist_to_nest_scout:
            self.position = self.home.position.copy()
            self.stop_food_trail()
            self.pheromone_strength = 0.
            self.increase_energy()
            at_nest = True

        return at_nest

    def at_food(self, noticeable_objects):
        """from abc import ABC, abstractmethod

        checks if ant is at food location, if True, load food and set has_food to loaded food
        :param noticeable_objects:
        :return: True if ant is at food position, else False
        """
        at_food = False

        # getting list of foods from noticeable objects
        foods = get_objects_of_type(noticeable_objects, Food)

        if foods:
            # print("no. food: "+str(len(foods)))
            for obj in foods:
                # print("distance to food: "+str(distance(self.position - obj.position)))
                if distance(self.position - obj.position) <= all_params.ant_model_params.min_dist_to_food_scout:
                    self.position = obj.position.copy()
                    self.start_food_trail()
                    self.pheromone_strength = min(200. * (obj.size / distance(self.position - self.home.position)),
                                                  self.max_pheromone_strength) / self.pheromone_dist_decay
                    at_food = True
                    break
        # print("at food: "+str(at_food))
        return at_food

    def stop_food_trail(self):
        """
        Set (found_food) variable to False when the ant reaches the nest and finishes the pheromone trail
        :return:
        """
        self.found_food = 0.  # TODO change to False when VIEW IS READY

    def start_food_trail(self):
        """
        set (found_food) variable to True when the ant finds food
        :return:
        """
        # print("food trail")
        self.found_food = 1.  # TODO change to True when VIEW IS READY

    def move_to_food(self, foods):
        """
        Selection of Food to move towards, and ant movement
        :param foods: (list) Food objects in noticeable objects
        :return: (array) new ant position
        """
        # Go directly to food if there is only one source
        if len(foods) == 1:
            return self.move_to(foods[0].position)

        # Compare food sources in terms of size and distance to nest
        else:
            sub_food = []
            for i, obj in enumerate(foods):
                # If food size equal to zero, we ignore the Food object
                if obj.size == 0:
                    pass
                # If distance is equal to zero, we ignore the Food object
                elif distance(obj.position - self.home.position) == 0:
                    pass
                else:
                    sub_food.append(obj)

            if sub_food:
                # Getting features of food objects
                data = zeros((len(sub_food), 2))
                for i, obj in enumerate(sub_food):
                    # Food size
                    data[i, 0] = obj.size
                    # Distance to nest
                    data[i, 1] = distance(obj.position - self.home.position)

                # Rescaling each feature to have values bounded by 1
                data /= np.max(data, axis=0)

                # Calculating probability distribution
                probs = (data[:, 0] ** self.foodiness) * (data[:, 1] ** self.explorativeness)
                probs /= np.sum(probs)

                # Drawing an object from the prob distribution
                index = np.random.choice(len(sub_food), p=probs)
                return self.move_to(sub_food[index].position)
            else:
                return None

    def move_randomly(self):
        chaos = 1.2
        seed = int(id(self) + time.time() * 2 ** chaos) % 2 ** 32
        np.random.seed(seed)
        return super().move_randomly()

    def move_to(self, obj_position):
        return super().move_to(obj_position)

    def set_trace(self, noticeable_objects):
        """
        if there is an existing pheromone in the position, add strength
        otherwise it will create a new pheromone
        :param noticeable_objects:
        :return: None if existing pheromone otherwise a new pheromone object
        """
        self.pheromone_strength = max(self.min_pheromone_strength,
                                      self.pheromone_dist_decay * self.pheromone_strength)
        for obj in noticeable_objects:
            if isinstance(obj, Pheromone):
                if distance(self.position - obj.position) <= all_params.ant_model_params.max_dist_to_pheromone:
                    obj.increase(added_strength=self.pheromone_strength)
                    return None
        else:
            # TODO implement pheromone type
            return Pheromone(self.position.copy(), self.owner,
                             initial_strength=self.pheromone_strength)  # , type='food')
