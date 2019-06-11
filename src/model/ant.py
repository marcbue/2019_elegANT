import numpy as np

from .food import Food
from .game_object import GameObject
from .pheromone import Pheromone

from src.utils import randint, array, get_objects_of_type, zeros
from src.settings import all_params

distance = np.linalg.norm


class Ant(GameObject):
    """
            A class used to represent an ant object
            It inherits from GameObject class

            ...

            Attributes
            ----------
            owner: Player
                Player object that the ant belongs to
            position: list
                a list of the ant coordinates
            has_food: float
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

    def __init__(self, player, home_nest):
        """Initialize ant object owner and position

        :param player: (Player) Owning Player of the ant
        :param home_nest: (Nest) Coordinates of ant position

        """
        position = home_nest.position.copy()
        super(Ant, self).__init__(position)
        self.owner = player
        # TODO: needs to be updated as well
        self.owner.ants.add(self)

        self.has_food = all_params.model_params.ant_has_food
        self.energy = all_params.model_params.ant_initial_energy
        self.direction = all_params.model_params.ant_initial_direction
        self.home = home_nest
        self.pheromone_strength = all_params.model_params.ant_initial_pheromone_strength

        # setting parameters
        self.loading_capacity = all_params.model_params.ant_loading_capacity
        self.min_pheromone_strength = all_params.model_params.min_pheromone_strength
        self.max_pheromone_strength = all_params.model_params.max_pheromone_strength
        self.pheromone_dist_decay = all_params.model_params.pheromone_dist_decay
        self.direction_memory = all_params.model_params.ant_direction_memory
        self.foodiness = all_params.model_params.ant_foodiness
        self.inscentiveness = all_params.model_params.ant_inscentiveness
        self.directionism = all_params.model_params.ant_directionism
        self.explorativeness = all_params.model_params.ant_explorativeness

    def __str__(self):
        return "Ant {} at position {} and energy lvl {} from player {}".format(self.id, self.position,
                                                                               self.energy, self.owner)

    def get_position(self):
        """
        Get the coordinates of the object ant position
        :return:
        """
        return self.position

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
        if self.energy <= all_params.model_params.ant_min_energy:
            return None, None

        if self.has_food:

            if self.at_nest():
                return self.position, None
            else:  # Go to nest if has food
                return self.move_to(self.home.position), self.set_trace(args[0])
        else:
            if self.at_food(args[0]):
                return self.position, None
            else:
                return self.move(args[0]), None

    def move(self, noticeable_objects):
        """
        Move the ant to a new position at each time iteration.
        If food is detected, movement is done in that direction. If no food is detected, pheromones are followed.
        Movement is random if there are no objects in visible objects.
        :param noticeable_objects: (list) All the possible objects that the ant can perceive
        :return: (array) Position to which the ant moves
        """

        # getting list of foods and pheromones from noticeable objects
        foods = get_objects_of_type(noticeable_objects, Food)
        pheromones = get_objects_of_type(noticeable_objects, Pheromone)

        # Priority is to get food
        if foods:
            return self.move_to_food(foods)

        # In case there is no food, pheromones are taken into account
        elif pheromones:
            return self.move_to_pheromone(pheromones)

        # In case there is no food nor pheromone scents, move randomly
        else:
            return self.move_randomly()

    def at_nest(self):
        """
        checks if ant is close enough to nest position, if True, unload food, and set pheromone strength to zero
        :return: True is ant is at nest position, otherwise False
        """
        at_nest = False

        if distance(self.position - self.home.position) <= all_params.model_params.ant_min_dist_to_nest:
            self.position = self.home.position.copy()
            self.unload_food()
            self.pheromone_strength = 0.
            at_nest = True

        return at_nest

    def at_food(self, noticeable_objects):
        """
        checks if ant is at food location, if True, load food and set has_food to loaded food
        :param noticeable_objects:
        :return: True if ant is at food position, else False
        """
        at_food = False

        # getting list of foods from noticeable objects
        foods = get_objects_of_type(noticeable_objects, Food)

        if foods:
            for obj in foods:
                if distance(self.position - obj.position) <= all_params.model_params.ant_min_dist_to_food:
                    self.position = obj.position.copy()
                    self.load_food(obj)
                    self.pheromone_strength = min(100. * (obj.size / distance(self.position - self.home.position)),
                                                  self.max_pheromone_strength) / self.pheromone_dist_decay
                    at_food = True
                    break

        return at_food

    def unload_food(self):  # TO DO
        """
        Flip (has_food) variable to 0 when the ant reaches the nest and unload the food
        :return:
        """
        self.home.increase_food(self.has_food)
        self.has_food = 0.

    def load_food(self, food):
        """
        increase (has_food) variable to loading capacity when the ant finds food
        :param food: the food object
        :return:
        """

        amount_taken = food.take_some(self.loading_capacity)
        self.has_food = amount_taken

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

    def move_to_pheromone(self, pheromones):
        """
        Selection of Pheromone to move towards, and ant movement
        :param pheromones: (list) Pheromone objects in noticeable objects
        :return: (array) new ant position
        """

        # Go directly to scent if there is only one source
        if len(pheromones) == 1:
            return self.move_to(pheromones[0].position)

        # Compare pheromone sources
        else:

            # Getting features of pheromone objects
            data = zeros((len(pheromones), 3))
            for i, obj in enumerate(pheromones):
                # Intensity
                data[i, 0] = obj.strength
                # Distance to nest
                data[i, 1] = distance(obj.position - self.home.position)
                # Difference in momentum
                # TODO define difference in momentum
                data[i, 2] = 1

            # Rescaling each feature to have values bounded by 1
            data /= np.max(data, axis=0)

            # Calculating probability distribution
            probs = (data[:, 0] ** self.inscentiveness) * (data[:, 1] ** self.explorativeness) \
                * (data[:, 2] ** self.directionism)
            probs /= np.sum(probs)

            # Draw an object from the prob distribution
            index = np.random.choice(len(pheromones), p=probs)
            return self.move_to(pheromones[index].position)

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
                if distance(self.position - obj.position) <= all_params.model_params.ant_max_dist_to_pheromone:
                    obj.increase(added_strength=self.pheromone_strength)
                    return None
        else:
            return Pheromone(self.position.copy(), self.owner, initial_strength=self.pheromone_strength)

    # TODO: This needs an update function that the world class can call for each ant. -- Unless move is going to
    #  handle food detection, loading, unloading, etc...
