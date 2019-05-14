import numpy as np
from scipy.spatial import cKDTree

from .ant import Ant
from .food import Food
from .nest import Nest
from .world import World


class KdTreeAndDict(World):

    """
            A class used to implement the tree and dictionary in the game (alternative to gird)
            It inherits from World class

            ...

            Attributes
            ----------
            all_objects: dict
                a dictionary for all the objects in the game
            kd_tree: cKDTree
                a tcKDTree implementation for nearest neighbours
            point_matrix: array
                an ### Add this

    """

    def __init__(self):
        self.all_objects = {}
        # TODO: check if None declaration
        # will not make trouble later
        self.kd_tree = None
        self.point_matrix = None

    def get_k_nearest(self, position, k=1):
        """ Get k nearest neighbour ants for specific position using kd_tree that uses Euclidean distance.

        :param position: (list) Coordinates of the position to which the nearest neighbours are calculated.
        :param k: (int) Number of nearest neighbours
        :return point_matrix: (array) ### Add this
        :return dists: (array of floats) Distances to the nearest neighbours

        """
        # TODO: can multithread if called with many params and -1
        dists, idx = self.kd_tree.query(position, k, p=2)
        dict_idxs = self.point_matrix[idx]
        if k == 1:
            game_object_list = self.all_objects.get(tuple(dict_idxs), [])
        else:
            game_object_list = [obj for idx in dict_idxs for obj in self.all_objects.get(tuple(idx))]
        return game_object_list, dists

    def get_at_position(self, position):
        """ Return all the objects (ants/food/nest) in specific position

        :param position: (list) Coordinates of specific position
        :return: (list) ALL objects in the given position

        """
        return self.all_objects.get(tuple(position))

    def get_rectangle_region(self, top_left, bottom_right):
        """

        :param top_left: (list) Coordinates of top left point of the rectangle
        :param bottom_right: (list) Coordinates of bottom right point of the rectangle
        :return:

        """
        longest_side = max(bottom_right[0] - top_left[0], top_left[1] - bottom_right[1])
        center = (top_left + bottom_right) / 2
        large_square_objects = self.get_square_region(center, longest_side)

        x_min = top_left[0]
        y_min = bottom_right[1]
        x_max = bottom_right[0]
        y_max = top_left[1]

        result = []
        for obj in large_square_objects:
            if self._is_in_rectangle(obj.position, x_min, x_max, y_min, y_max):
                result.append(obj)
        return result

    def get_circular_region(self, center, radius):
        position_idx = self.kd_tree.query_ball_point(center, radius, p=2)
        positions = self.point_matrix[position_idx]
        result = []
        for position in positions:
            result.extend(self.all_objects.get(tuple(position)))
        return result

    def get_k_nearest_list(self, position_list, k):
        # TODO: can multithread if called with many params and -1
        if len(position_list) == 1:
            return self.get_k_nearest(position_list, k)
        dists, idx_list = self.kd_tree.query(position_list, k, p=2)
        result = []
        for array in idx_list:
            if len(array.shape) == 0:
                dict_ind = self.point_matrix[array]
                result.append(self.all_objects[tuple(dict_ind)])
            else:
                dict_ind = self.point_matrix[array]
                sub_result = [obj for row in dict_ind for obj in self.all_objects[tuple(row)]]
                result.append(sub_result)

        return result, dists

    def get_rectangle_region_list(self, top_left_list, bottom_right_list):
        #
        pass

    def get_circular_region_list(self, center_list, radius_list):
        position_idx_list = self.kd_tree.query_ball_point(center_list, radius_list, p=2)
        result = []
        for position_idx in position_idx_list:
            positions = self.point_matrix[position_idx]
            sub_result = []
            for position in positions:
                sub_result.extend(self.all_objects.get(tuple(position)))
            result.append(sub_result)
        return result

    def update(self):
        all_lists = list(self.all_objects.values())
        for listy in all_lists:
            for item in listy:
                if type(item) == Ant:
                    item.move() # TODO: switch to update() when implemented
        self._update_tree()

    def create_nests(self, color_list, position_list, size, health):
        for position, color in zip(position_list, color_list):
            self.all_objects.setdefault(tuple(position), []).append(Nest(position, color, size, health))
        self._update_tree()

    def create_ants(self, nest, amount):
        position = nest.position
        color = nest.color
        for _ in range(amount):
            self.all_objects.setdefault(tuple(position), []).append(Ant(color, position))
        self._update_tree()

    def create_food(self, position_list, size_list):
        # TODO: compare to extend with food list
        for position, size in zip(position_list, size_list):
            self.all_objects.setdefault(tuple(position), []).append(Food(position, size))
        self._update_tree()

    def dump_content(self):
        everything = list(self.all_objects.values())
        flat_everything = [obj for listy in everything for obj in listy]
        return flat_everything

    def _update_tree(self):
        keys = list(self.all_objects.keys())
        self.point_matrix = np.array(keys)
        self.kd_tree = cKDTree(self.point_matrix)

    def get_square_region(self, center, radius):
        position_idx = self.kd_tree.query_ball_point(center, radius, p=np.inf)
        positions = self.point_matrix[position_idx]
        result = []
        for position in positions:
            result.extend(self.all_objects.get(tuple(position)))
        return result

    def _is_in_rectangle(self, position, x_min, x_max, y_min, y_max):
        return x_min <= position[0] <= x_max and y_min <= position[1] <= y_max
