from src.view.view import View


def test_view_name():
    view = View(1300, 800)
    assert not view.state


def test_view_size():
    view = View(1300, 800)
    assert view.size == (1300, 800)
