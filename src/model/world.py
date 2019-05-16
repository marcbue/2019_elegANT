# Interface used by GameState
# Implementation is done currently by KdTreeAndDict
from abc import ABC, abstractmethod


class World(ABC):

    @abstractmethod
    def get_k_nearest(self, position, k):
        # Inheriting class should return k nearest neighbours of the passed position
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def get_at_position(self, position):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def get_rectangle_region(self, top_left, bottom_right):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def get_circular_region(self, center, radius):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def get_k_nearest_list(self, position_list, k):
        # Inheriting class should return k nearest neigbours of the passed position
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def get_circular_region_list(self, center_list, radius_list):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def update(self):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def create_nests(self, color_list, position_list, size, health):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def create_ants(self, nest, amount):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def create_food(self, position_list, size_list):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def dump_content(self):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def get_ants(self):
        raise NotImplementedError("Please use subclassing.")

    @abstractmethod
    def get_nests(self):
        raise NotImplementedError("Please use subclassing.")

