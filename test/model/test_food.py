from src.model.food import Food
import pytest
import array


@pytest.fixture
def set_up_init_food_fixed():
    position = array.array('f', [0.5, 0.5])
    size1 = 5
    size2 = -2
    return position, size1, size2


def test__init__(set_up_init_food_fixed):
    position, size1, size2 = set_up_init_food_fixed
    food = Food(position, size1)
    assert food.position[:] == position[:] and food.size == size1


def test_update_food(set_up_init_food_fixed):
    position, size1, size2 = set_up_init_food_fixed
    food1 = Food(position, size1)
    new_position1 = food1.update(size1)
    assert new_position1[:] == position[:]
    food2 = Food(position, size2)
    new_position2 = food2.update(size2)
    assert new_position2 is None
