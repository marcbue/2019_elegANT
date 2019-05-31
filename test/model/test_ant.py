from src.model.ant import Ant
from src.model.nest import Nest
from src.model.player import Player
from src.utils import array
import numpy as np

player = Player(name="Nobody", color="blue")
nest = Nest(position=array([0, 0]), player=player, size=10, health=100)
ant = Ant(player=player, home_nest=nest)


def test_move_has_food():
    ant.has_food = 1
    ant.position = array([10, 0])
    position = ant.move([])
    # asserting that y-move is towards the nest
    assert np.isclose(position, array([9, 0])).all(), 'incorrect y-move direction'
    # asserting that the position is updated
    assert np.isclose(ant.position, position).all(), 'position not updated'
    ant.position = array([0, 10])
    position = ant.move([])
    # asserting that x-move is towards the nest
    assert np.isclose(position, array([0, 9])).all(), 'incorrect x-move direction'
    ant.position = array([0, 0])
    position = ant.move([])
    assert np.isclose(position, array([0, 0])).all(), 'moves after reaching the object'


def test_move_randomly():
    ant.has_food = 0
    ant.position = array([0, 0])
    ant.direction = array([0, 0])
    previous_position = array(ant.position)
    position = ant.move([])
    assert np.isclose(position, ant.position).all(), 'position not updated'
    assert np.isclose(1, np.linalg.norm(ant.direction)).all(), 'direction not one: %r' % ant.direction
    assert np.isclose(1, np.linalg.norm(ant.position - previous_position)).all(), 'movement not one: %r' % ant.position
