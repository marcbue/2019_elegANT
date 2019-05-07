import numpy as np
from scipy.spatial import cKDTree

from .ant import Ant
from .food import Food
from .nest import Nest
from .world import World


class KdTreeAndDict(World):
    def __init__(self):
        self.all_objects = {}
        self.kd_tree = cKDTree()

    def get_k_nearest(self, position):
        # Inheriting class should return k nearest neigbours of the passed position
        pass

    def get_rectangle_region(self, top_left, bottom_right):
        #
        pass

    def get_circular_region(self, center, radius):
        pass

    def get_k_nearest_list(self, position_list):
        # Inheriting class should return k nearest neigbours of the passed position
        pass

    def get_rectangle_region_list(self, top_left_list, bottom_right_list):
        #
        pass

    def get_circular_region_list(self, center_list, radius_list):
        pass

    def update(self):
        pass

    def create_nests(self, color_list, position_list, size=10, health=100):
        for position, color in zip(position_list, color_list):
            self.all_objects.setdefault(position, []).append(Nest(position, color, size, health))
        self._update_tree()

    def create_ants(self, nest, amount):
        position = nest.position
        color = nest.color
        for _ in len(amount):
            self.all_objects.setdefault(position, []).append(Ant(color, position))
        self._update_tree()

    def create_food(self, position_list, size_list):
        # TODO: compare to extend with food list
        for position, size in zip(position_list, size_list):
            self.all_objects.setdefault(position, []).append(Food(position, size))
        self._update_tree()

    def _update_tree(self):
        keys = list(self.all_objects.keys())
        position_matrix = np.array(keys)
        self.kd_tree = cKDTree(position_matrix)
