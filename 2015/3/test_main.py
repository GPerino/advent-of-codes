from unittest import TestCase

from main import define_next_coordinates, Santa


def create_santa_instance():
    santa = Santa(0, 0)
    assert santa.x == 0
    assert santa.x == 0


class Test(TestCase):

    def test_returns_to_origin(self):
        assert define_next_coordinates("^>v<") == (0, 0)

    def test_go_up(self):
        assert define_next_coordinates("^") == (0, 1)

    def test_go_down(self):
        assert define_next_coordinates("v") == (0, -1)

    def test_go_left(self):
        assert define_next_coordinates("<") == (-1, 0)

    def test_go_right(self):
        assert define_next_coordinates(">") == (1, 0)
