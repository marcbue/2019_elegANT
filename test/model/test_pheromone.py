import pytest

from src.model.pheromone import Pheromone
from src.model.player import Player
from src.utils import array


@pytest.fixture
def set_up_pheromone():
    position = array([5, 5])
    player = Player("Nobody", (178, 58, 238))
    test_pheromone = Pheromone(position, player)
    return (position, player, test_pheromone)


def test_init__(set_up_pheromone):
    position, player, test_pheromone = set_up_pheromone
    assert ((test_pheromone.position == position).all())
    assert (test_pheromone.owner == player)
    assert (test_pheromone.strength > 0)

    initial_strength = 10
    test_pheromone2 = Pheromone(position, player, initial_strength)
    assert (test_pheromone2.strength == initial_strength)


def test_update(set_up_pheromone):
    position, player, test_pheromone = set_up_pheromone
    while test_pheromone.strength > 0:
        old_strength = test_pheromone.strength
        returned_position = test_pheromone.update()
        assert (test_pheromone.strength < old_strength)
    assert (returned_position is None)


def test_increase(set_up_pheromone):
    position, player, test_pheromone = set_up_pheromone
    old_strength = test_pheromone.strength
    test_pheromone.increase()
    assert (old_strength < test_pheromone.strength)
    old_strength = test_pheromone.strength
    increase = 5
    test_pheromone.increase(increase)
    assert (test_pheromone.strength == old_strength + increase)


@pytest.mark.xfail(strict=True)
def test_invalid_increase(set_up_pheromone):
    position, player, test_pheromone = set_up_pheromone
    test_pheromone.increase(-5)
