from unittest import TestCase

from main import calculate_hash, find_lowest_number_from_secret


class Test(TestCase):


    def test_abcdef_lowest_number(self):
        assert find_lowest_number_from_secret("abcdef") == 609043

    def test_pqrstuv_lowest_number(self):
        assert find_lowest_number_from_secret("pqrstuv") == 1048970

    def test_abcdef_verify(self):
        assert calculate_hash("abcdef609043") == "000001dbbfa3a5c83a2d506429c7b00e"

    def test_pqrstuv_verify(self):
        assert calculate_hash("pqrstuv1048970") == "000006136ef2ff3b291c85725f17325c"
