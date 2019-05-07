from .world import World
from scipy.spatial import cKDTree

class KdTreeAndDict(World):
    def __init__(self):
        self.all_objects = {}
        self.kd_tree = cKDTree()


