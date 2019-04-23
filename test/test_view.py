from src.view.view import View
import pygame


def test_view_name():
    view = View()
    assert view.view == "start_screen"


def test_view_size():
    view = View()
    assert view.size == (329, 249)

