from unittest import TestCase

from main import define_next_coordinates, discover


class Test(TestCase):

    def test_go_up(self):
        assert define_next_coordinates("^") == (0, 1)

    def test_go_down(self):
        assert define_next_coordinates("v") == (0, -1)

    def test_go_left(self):
        assert define_next_coordinates("<") == (-1, 0)

    def test_go_right(self):
        assert define_next_coordinates(">") == (1, 0)

    def test_discover_2_houses(self):
        assert discover("^") == 2

    def test_discover_4_distinct_houses(self):
        assert discover("^>v<") == 4

    def test_2_houses(self):
        assert discover("^v^v^v^v^v") == 2

    def test_test_file(self):
        assert discover(">^^v^<>v<<<v<v^>>v^") == 13

    def test_7_come_and_go_houses(self):
        assert discover("^><>v><>v<") == 7
