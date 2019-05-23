from src.model.food import Food
import pytest
import array


@pytest.fixture
def food_creation_fixed():
    position = array.array('f', [0.5, 0.5])
    size = 5
    return (position, size)


def test_food_creation(food_creation_fixed):
    position, size = food_creation_fixed
    nest = Food(position, size)
    assert nest.position[:] == position[:] and nest.size == size
