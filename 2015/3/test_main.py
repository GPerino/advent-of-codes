from unittest import TestCase

from main import define_next_coordinates, Santa


def create_santa_instance():
    santa = Santa(0, 0)
    assert santa.x == 0
    assert santa.x == 0


class Test(TestCase):
    def test_define_directions(self):
        self.fail()
