import numpy as np
from src.utils import array


class ControllerParams:

    def __init__(self, framerate=30):
        super(ControllerParams, self).__init__()
        self.framerate = framerate
        self.create_ant_time = 2


class ModelParams:

    def __init__(self):
        super(ModelParams, self).__init__()
        self.food_min_size = 0.
        self.nest_initial_food = 0.
        self.creating_ant_cost = 1.
        self.nest_min_health = 0.
        self.pheromone_initial_strength = 1.
        self.pheromone_min_strength = 1e-8
        self.pheromone_added_strength = 1.
        self.pheromone_decay_factor = 0.75
        self.ant_has_food = 0.
        self.ant_initial_energy = 100.
        self.ant_initial_direction = array([0., 0.])
        self.ant_initial_pheromone_strength = 0.
        self.ant_loading_capacity = 1.
        self.min_pheromone_strength = 1.
        self.max_pheromone_strength = 10.
        self.pheromone_dist_decay = 0.95
        self.ant_direction_memory = 0.5
        self.ant_foodiness = 1.
        self.ant_inscentiveness = 1.
        self.ant_directionism = 1.
        self.ant_explorativeness = 1.
        self.ant_min_energy = 0.
        self.ant_min_dist_to_nest = 1.
        self.ant_min_dist_to_food = 1.
        self.ant_max_dist_to_pheromone = 1.
        self.circular_region_radius = 10
        self.tree_distance_type = 2
        self.circular_region_distance = 2
        self.square_region_distance = np.inf


class ViewParams:

    def __init__(self):
        super(ViewParams, self).__init__()


class AllParams:

    def __init__(self, controller_params, model_params, view_params):
        self.controller_params: ControllerParams = controller_params
        self.model_params: ModelParams = model_params
        self.view_params: ViewParams = view_params


c_p = ControllerParams()
m_p = ModelParams()
v_p = ViewParams()

all_params = AllParams(controller_params=c_p,
                       model_params=m_p,
                       view_params=v_p
                       )
