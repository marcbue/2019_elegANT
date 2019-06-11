from src.model.ant import Ant
from src.model.nest import Nest
from src.model.food import Food
from src.model.player import Player
from src.model.pheromone import Pheromone
from src.utils import array
import numpy as np
import pytest


# TODO it would be best if all tests only call update function to make sure update logic is correct


@pytest.fixture
def set_up_environment():
    player = Player(name="Nobody", color=(178, 58, 238))
    nest = Nest(position=array([0., 0.]), player=player, size=10., health=100.)
    ant = Ant(player=player, home_nest=nest)
    return player, nest, ant


@pytest.fixture
def set_up_pheromones():
    player = Player("Nobody", (178, 58, 238))
    position = array([5., 5.])
    intensity = 20.
    pheromone1 = Pheromone(position, player, intensity)
    position = array([4., 5.])
    intensity = 10.
    pheromone2 = Pheromone(position, player, intensity)
    pheromones = [pheromone1, pheromone2]
    return pheromones


@pytest.fixture
def set_up_ants(set_up_environment):
    player, nest, ant = set_up_environment
    return [ant] * 5


@pytest.fixture
def set_up_foods():
    player = Player("Nobody", (178, 58, 238))
    position = array([5., 5.])
    intensity = 20.
    pheromone1 = Pheromone(position, player, intensity)
    position = array([4., 5.])
    intensity = 10.
    pheromone2 = Pheromone(position, player, intensity)
    pheromones = [pheromone1, pheromone2]
    return pheromones


# should this be removed?
def set_up_food_fixed():
    position = array([0.5, 0.5])
    size1 = 5.
    size2 = -2.
    return position, size1, size2


@pytest.fixture
def set_up_food():
    food = Food(position=array([13., 17.]), size=1)
    return food


def test_move_has_food(set_up_environment):
    player, nest, ant = set_up_environment
    ant.has_food = 1.

    # asserting that y-move is towards the nest
    ant.position = array([10., 0.])
    position, _ = ant.update([])
    assert np.isclose(position, array([9., 0.])).all(), 'incorrect y-move direction'

    # asserting that x-move is towards the nest
    ant.position = array([0., 10.])
    position, _ = ant.update([])
    assert np.isclose(position, array([0., 9.])).all(), 'incorrect x-move direction'

    # asserting the arrival
    ant.position = array([0., 0.])
    position, _ = ant.update([])
    assert np.isclose(position, array([0., 0.])).all(), 'moves after reaching the object'


def test_move_randomly(set_up_environment):
    player, nest, ant = set_up_environment
    ant.has_food = 0.
    ant.position = array([0., 0.])
    ant.direction = array([0., 0.])
    init_position = array(ant.position)
    position, _ = ant.update([])
    assert np.isclose(1., np.linalg.norm(ant.direction)), 'direction not one: %r' % ant.direction
    assert np.isclose(1., np.linalg.norm(ant.position - init_position)), 'movement not one: %r' % ant.position


def test_unload_food(set_up_environment):
    player, nest, ant = set_up_environment
    ant.has_food = 1.
    ant.position = array([0., 0.])
    init_nest_food = nest.food
    init_ant_food = ant.has_food
    ant.unload_food()
    assert ant.has_food == 0., 'food is not unloaded'
    assert nest.food == (init_ant_food + init_nest_food), 'some food is lost in unloading'


def test_load_food(set_up_environment, set_up_food):
    player, nest, ant = set_up_environment
    food = set_up_food

    # testing when the food is larger than ant's loading capacity
    food.size = 2. * ant.loading_capacity
    init_food_size = food.size
    ant.load_food(food=food)
    assert food.size + ant.has_food == init_food_size, 'some food is lost in loading'

    # testing if food size is smaller than ant's loading capacity
    ant.has_food = 0.
    food.size = 0.5 * ant.loading_capacity
    init_food_size = food.size
    ant.load_food(food=food)
    assert food.size == 0., 'ant did not take all the possible load'
    assert ant.has_food == init_food_size, 'ant did not take all the food'


def test_get_position(set_up_environment):
    player, nest, ant = set_up_environment
    init_position = ant.get_position()
    ant.has_food = 0.
    ant_position, _ = ant.update([])
    new_position = ant.get_position()
    assert np.isclose(0., np.linalg.norm(ant_position - new_position)), 'ant position is not updated'
    assert np.isclose(1., np.linalg.norm(new_position - init_position)), 'ant did not move in steps on one'
