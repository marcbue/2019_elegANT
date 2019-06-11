from src.model.nest import Nest
from src.model.player import Player
import pytest
from src.utils import array


@pytest.fixture
def nest_creation_fixed():
    position = array([0.5, 0.5])
    player = Player(name="Nobody", color=(178, 58, 238))
    size = 5
    health = 10
    return (position, player, size, health)


def test_nest_creation(nest_creation_fixed):
    position, player, size, health = nest_creation_fixed
    nest = Nest(position, player, size, health)
    assert (nest.position == position).all()
    assert nest.owner == player
    assert nest.size == size
    assert nest.health == health


@pytest.fixture
def set_up_nest():
    position = array([0.5, 0.5])
    color = (178, 58, 238)
    size = 5
    health = 10
    return position, color, size, health


def test_increase_food(set_up_nest):
    position, color, size, health = set_up_nest
    food_amount = 3.5
    nest = Nest(position, color, size, health)
    nest.increase_food(food_amount)
    amount_tested = nest.food
    assert food_amount == amount_tested


# def test_create_ant():
#     position, color, size, health = set_up_nest
#     nest = Nest(position, color, size, health)
#     food_amount = set_up_food_fixed
#     assert


def test_decrease_health(set_up_nest):
    position, color, size, health = set_up_nest
    damage = 5
    nest = Nest(position, color, size, health)
    nest.decrease_health(damage)
    assert nest.health == health - damage


# def test_get_number_of_ants():
#     assert
#


def test_update(set_up_nest):
    health1 = 5
    health2 = -3
    position, color, size, health = set_up_nest
    nest1 = Nest(position, color, size, health1)
    new_position1 = nest1.update(health1)
    assert ((new_position1 == position).all())
    nest2 = Nest(position, color, size, health2)
    new_position2 = nest2.update(health2)
    assert new_position2 is None
