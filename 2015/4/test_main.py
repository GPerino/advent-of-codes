from unittest import TestCase

from main import calculate_hash, find_lowest_number_from_secret


class Test(TestCase):
    def test_abcdef_verify(self):
        assert calculate_hash("abcdef6742839").startswith("000000")

    def test_pqrstuv_verify(self):
        assert calculate_hash("pqrstuv5714438").startswith("000000")
