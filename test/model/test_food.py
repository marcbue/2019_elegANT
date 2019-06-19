from src.model.food import Food
import pytest
from src.utils import array


@pytest.fixture
def set_up_food_fixed():
    position = array([0.5, 0.5])
    size = 5
    return position, size


def test_init__(set_up_food_fixed):
    position, size = set_up_food_fixed
    food = Food(position, size)
    assert ((food.position == position).all())
    assert food.size == size


def test_update(set_up_food_fixed):
    size2 = -5
    position, size = set_up_food_fixed
    food1 = Food(position, size)
    new_position1 = food1.update(size)
    assert ((new_position1 == position).all())
    food2 = Food(position, size2)
    new_position2 = food2.update(size2)
    assert new_position2 is None
