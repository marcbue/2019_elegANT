from src.utils import array


class ControllerParams:

    def __init__(self, framerate=30):
        super(ControllerParams, self).__init__()
        self.framerate = framerate
        self.create_ant_time = 1


class ModelParams:

    def __init__(self):
        super(ModelParams, self).__init__()


class AntModelParams:

    def __init__(self):
        super(AntModelParams, self).__init__()
        # Energy
        # self.initial_energy = 100.  # TODO remove when different initial values per ant are created
        self.energy_increase = 10.
        self.maximum_energy = 1000.
        self.min_energy = 0.

        # Pheromone
        # self.initial_pheromone_strength = 0.
        self.initial_direction = array([0., 0.])
        self.min_pheromone_strength = 1.
        self.max_pheromone_strength = 100.
        self.pheromone_dist_decay = 0.95

        # Food
        # self.loading_capacity = 1.

        # Movement and distances
        self.direction_memory = 0.75
        self.min_dist_to_nest = 1.5
        self.min_dist_to_food = 1.5
        self.min_dist_to_nest_scout = 4.
        self.min_dist_to_food_scout = 4.
        self.max_dist_to_pheromone = 1.

        # Ant features
        # self.foodiness = 1.
        # self.inscentiveness = 1.
        # self.directionism = 1.
        # self.explorativeness = 1.


class FoodModelParams:

    def __init__(self):
        super(FoodModelParams, self).__init__()
        self.min_size = 0.


class NestModelParams:

    def __init__(self):
        super(NestModelParams, self).__init__()
        self.initial_food = 0.
        self.create_ant_cost = 1.
        self.min_health = 0.


class PheromoneModelParams:

    def __init__(self):
        super(PheromoneModelParams, self).__init__()
        self.initial_strength = 1.  # TODO comment out initial_strength after pheromone.py an ABC
        self.min_strength = 1e-8
        self.added_strength = 1
        self.decay_factor = 0.75


class TreeModelParams:

    def __init__(self):
        super(TreeModelParams, self).__init__()
        self.circular_region_radius_scout = 60
        self.circular_region_radius_worker = 30


class ViewParams:

    def __init__(self):
        super(ViewParams, self).__init__()


class AllParams:

    def __init__(self, controller_params, model_params, ant_model_params, food_model_params, nest_model_params,
                 pheromone_model_params, tree_model_params, view_params):
        self.controller_params: ControllerParams = controller_params
        self.model_params: ModelParams = model_params
        self.ant_model_params: AntModelParams = ant_model_params
        self.food_model_params: FoodModelParams = food_model_params
        self.nest_model_params: NestModelParams = nest_model_params
        self.pheromone_model_params: PheromoneModelParams = pheromone_model_params
        self.tree_model_params: TreeModelParams = tree_model_params
        self.view_params: ViewParams = view_params


c_p = ControllerParams()

m_p = ModelParams()
a_mp = AntModelParams()
f_mp = FoodModelParams()
n_mp = NestModelParams()
p_mp = PheromoneModelParams()
t_mp = TreeModelParams()

v_p = ViewParams()

all_params = AllParams(controller_params=c_p,
                       model_params=m_p,
                       ant_model_params=a_mp,
                       food_model_params=f_mp,
                       nest_model_params=n_mp,
                       pheromone_model_params=p_mp,
                       tree_model_params=t_mp,
                       view_params=v_p
                       )
