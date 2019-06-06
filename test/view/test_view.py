from src.view.view import View


def test_view_initialization():
    view = View(1300, 800)
    assert not view.state


def test_view_state():
    view = View(1300, 800)
    view.state = 'start-view'
    assert view.state == 'start-view'


def test_view_size():
    view = View(1300, 800)
    assert view.width == 1300 and view.height == 800
