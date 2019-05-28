from src.model.nest import Nest
from src.model.player import Player
import pytest
import array


@pytest.fixture
def nest_creation_fixed():
    position = array.array('f', [0.5, 0.5])
    player = Player(name="Nobody", color="red")
    size = 5
    health = 10
    return (position, player, size, health)


def test_nest_creation(nest_creation_fixed):
    position, player, size, health = nest_creation_fixed
    nest = Nest(position, player, size, health)
    assert nest.position[:] == position[:] and nest.owner == player and nest.size == size and nest.health == health


@pytest.fixture
def increase_food_fixed():
    food_amount = 0.5
    return food_amount


def test_increase_food(increase_food_fixed):
    food_amount = increase_food_fixed
    position = array.array('f', [0.5, 0.5])
    nest = Nest(position, "red", 2, 1)
    amount_tested = nest.increase_food(0.5)
    assert food_amount == amount_tested


# def test_create_ant():
#     assert
#
#
# def test_decrease_health():
#     assert
#
#
# def test_get_number_of_ants():
#     assert
#
# def test_update():
#     assert
