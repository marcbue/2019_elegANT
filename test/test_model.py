from src.model.model import Player

name = "franz"
color = "red"


def test_model_creation():
    player = Player(name, color)
    assert player.name == name and player.color == color


def test_name_setter():
    player = Player(name, color)
    new_name = "herbert"
    player.set_name(new_name)
    assert player.name == new_name


def test_name_getter():
    player = Player(name, color)
    assert player.get_name() == name


def test_color_setter():
    player = Player(name, color)
    new_color = "herbert"
    player.set_color(new_color)
    assert player.color == new_color


def test_color_getter():
    player = Player(name, color)
    assert player.get_color() == color


def test_data_storage():
    player = Player(name, color)
    player.store_data()
    player2 = Player(name, color)
    player2.read_data(filename=str(name) + ".p")
    assert player.__dict__ == player2.__dict__
