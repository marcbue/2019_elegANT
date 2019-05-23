from src.model.nest import Nest
import pytest
import array


@pytest.fixture
def nest_creation_fixed():
    position = array.array('f', [0.5, 0.5])
    color = "red"
    size = 5
    health = 10
    return (position, color, size, health)


def test_nest_creation(nest_creation_fixed):
    position, color, size, health = nest_creation_fixed
    nest = Nest(position, color, size, health)
    assert nest.position[:] == position[:] and nest.color == color and nest.size == size and nest.health == health


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
