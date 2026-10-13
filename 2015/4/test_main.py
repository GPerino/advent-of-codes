from unittest import TestCase

from main import main

class Test(TestCase):

    def test_abcdef_render(self):
        assert main == 609043
