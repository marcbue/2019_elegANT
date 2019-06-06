from src.model.ant import Ant
from src.model.nest import Nest
# from src.model.food import Food
from src.model.player import Player
from src.model.pheromone import Pheromone
from src.utils import array
import numpy as np
import pytest


@pytest.fixture
def setup_environment():
    player = Player(name="Nobody", color=(178, 58, 238))
    nest = Nest(position=array([0., 0.]), player=player, size=10., health=100.)
    ant = Ant(player=player, home_nest=nest)
    return player, nest, ant


@pytest.fixture
def set_up_pheromones():
    player = Player("Nobody", (178, 58, 238))
    position = array([5, 5])
    intensity = 20.
    pheromone1 = Pheromone(position, player, intensity)
    position = array([4, 5])
    intensity = 10.
    pheromone2 = Pheromone(position, player, intensity)
    pheromones = [pheromone1, pheromone2]
    return pheromones


@pytest.fixture
def set_up_ants(setup_environment):
    player, nest, ant = setup_environment
    return [ant] * 5


@pytest.fixture
def set_up_foods():
    player = Player("Nobody", (178, 58, 238))
    position = array([5, 5])
    intensity = 20.
    pheromone1 = Pheromone(position, player, intensity)
    position = array([4, 5])
    intensity = 10.
    pheromone2 = Pheromone(position, player, intensity)
    pheromones = [pheromone1, pheromone2]
    return pheromones


def set_up_food_fixed():
    position = array([0.5, 0.5])
    size1 = 5
    size2 = -2
    return position, size1, size2


def test_move_has_food(setup_environment):
    player, nest, ant = setup_environment
    ant.has_food = 1.
    ant.position = array([10., 0.])
    position = ant.move([])
    # asserting that y-move is towards the nest
    assert np.isclose(position, array([9., 0.])).all(), 'incorrect y-move direction'
    # asserting that the position is updated
    assert np.isclose(ant.position, position).all(), 'position not updated'
    ant.position = array([0., 10.])
    position = ant.move([])
    # asserting that x-move is towards the nest
    assert np.isclose(position, array([0., 9.])).all(), 'incorrect x-move direction'
    ant.position = array([0., 0.])
    position = ant.move([])
    assert np.isclose(position, array([0., 0.])).all(), 'moves after reaching the object'


def test_move_randomly(setup_environment):
    player, nest, ant = setup_environment
    ant.has_food = 0.
    ant.position = array([0., 0.])
    ant.direction = array([0., 0.])
    previous_position = array(ant.position)
    position = ant.move([])
    assert np.isclose(position, ant.position).all(), 'position not updated'
    assert np.isclose(1, np.linalg.norm(ant.direction)).all(), 'direction not one: %r' % ant.direction
    assert np.isclose(1, np.linalg.norm(ant.position - previous_position)).all(), 'movement not one: %r' % ant.position


def test_unload_food(setup_environment):
    player, nest, ant = setup_environment
    ant.has_food = 1.
    ant.position = array([0., 0.])
    ant.unload_food()
    assert ant.has_food == 0., 'food is not unloaded'

