import pytest
from src.model.game_state import GameState
from src.model.player import Player
from src.model.food import Food
from src.utils import array


@pytest.fixture
def set_up_game_state_fixed():
    """Initializes and returns GameState with one player"""
    players = [Player("Nobody", (0, 0, 0))]
    game_state = GameState(players)
    return players, game_state


def test___init__(set_up_game_state_fixed):
    players, game_state = set_up_game_state_fixed
    content = game_state.world.dump_content()
    foods = [obj for obj in content if type(obj) == Food]
    assert len(foods) == 50
    assert len(game_state.get_nests()) == len(players)
    assert len(game_state.get_ants()) == 0


def test_generate_random_food(set_up_game_state_fixed):
    players, game_state = set_up_game_state_fixed
    content = game_state.world.dump_content()
    old_foods = [obj for obj in content if type(obj) == Food]
    top_left = array([-10, 10])
    bottom_right = array([10, -10])
    amount = 10
    sizes = list(range(10))
    game_state.generate_random_food(top_left, bottom_right, amount, sizes)
    content = game_state.world.dump_content()
    new_foods = [obj for obj in content if type(obj) == Food]
    assert len(new_foods) == len(old_foods) + amount

    def in_range(position):
        x_good = top_left[0] <= position[0] <= bottom_right[0]
        y_good = top_left[1] >= position[1] >= bottom_right[1]
        return x_good and y_good

    for food in new_foods:
        assert food in old_foods or (in_range(food.position) and food.size in sizes)
        if food not in old_foods:
            sizes.remove(food.size)

    assert len(sizes) == 0
