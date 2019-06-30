from src.controller.controller import Controller


def create_game_state():
    c = Controller()
    game_state = c.start_button_pressed(color=(87, 112, 219), player_name='Ash')
    return game_state


def test_create_game_state():
    game_state = create_game_state()
    assert game_state


def test_press_start_button_and_no_player_name():
    c = Controller()
    game_state = c.start_button_pressed(color=(87, 112, 219), player_name='')
    assert game_state is None


