from abc import ABC, abstractmethod


class World(ABC):

    @abstractmethod
    def get_k_nearest(self, position):
        # Inheriting class should return k nearest neigbours of the passed position
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def get_rectangle_region(self, top_left, bottom_right):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def get_circular_region(self, center, radius):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def get_k_nearest_list(self, position_list):
        # Inheriting class should return k nearest neigbours of the passed position
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def get_rectangle_region_list(self, top_left_list, bottom_right_list):
        #
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def get_circular_region_list(self, center_list, radius_list):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def update(self):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def create_nests(self, color_list, position_list):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def create_ants(self, nest, amount):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def create_food(self, position_list, size_list):
        raise NotImplementedError("Please use subclassing.")
