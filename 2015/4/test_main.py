from unittest import TestCase

from main import calculate_hash, find_lowest_number_from_secret


class Test(TestCase):

    def test_abcdef_lowest_number(self):
        assert find_lowest_number_from_secret("abcdef") == 6742839

    def test_pqrstuv_lowest_number(self):
        assert find_lowest_number_from_secret("pqrstuv") == 5714438

    def test_abcdef_verify(self):
        assert calculate_hash("abcdef6742839") == "000000072a1e4320d13deee9d934ae29"
        assert calculate_hash("abcdef6742839").startswith("000000")

    def test_pqrstuv_verify(self):
        assert calculate_hash("pqrstuv5714438") == "000000c76bdbbb114044ada5ad14523b"
        assert calculate_hash("pqrstuv5714438").startswith("000000")

