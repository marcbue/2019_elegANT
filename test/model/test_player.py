from src.model.player import Player
# from src.model.ant import Ant
# from src.model.nest import Nest
import pytest


@pytest.fixture
def set_up_player():
    name = "franz"
    color = (0, 0, 0)
    return name, color


@pytest.fixture
def change_player():
    name = "herbert"
    color = (178, 58, 238)
    return name, color


def test_init__(set_up_player):
    name, color = set_up_player
    player = Player(name, color)
    assert player.name == name and player.color == color


def test_name_setter_and_getter(set_up_player, change_player):
    name, color = set_up_player
    player = Player(name, color)
    assert player.name == name
    new_name, new_color = change_player
    player.name = new_name
    assert player.name == new_name


def test_color_setter_and_getter(set_up_player, change_player):
    name, color = set_up_player
    player = Player(name, color)
    assert player.color == color
    new_name, new_color = change_player
    player.color = new_color
    assert player.color == new_color


def test_data_storage(set_up_player):
    name, color = set_up_player
    player = Player(name, color)
    player.store_data()
    player2 = Player(name, color)
    player2.read_data(filename=str(name) + ".p")
    assert player.__dict__ == player2.__dict__


# def test_owning_ants(set_up_player):  # TODO
#     player_name, color = set_up_player
#     player = Player(player_name, color)
#     print(player)
#     # Check that there are no ants.
#     assert not bool(player.ants)
#     nest = Nest([0, 0], player, 1, 100)
#     player.ants.add(Ant(player, nest))
#     assert bool(player.ants)
