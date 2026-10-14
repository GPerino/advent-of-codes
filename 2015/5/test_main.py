from unittest import TestCase

from main import check_character, check_double_pair, check_contains_repeated_letter

class Test(TestCase):

    def test_naughty_string(self):
        assert check_character("qjhvhtzxzqqjkmpb") == True  # corresponding twice rules
        assert check_character("xxyxx") == True  # corresponding twice rules
        assert check_character("uurcxstgmygtbstg") == False  # one pair only
        assert check_character("ieodomkazucvgmuy") == False  # no repeated letter

    def test_must_contains_double_pair(self):
        assert check_double_pair("aabcdefgaa") == True
        assert check_character("qjhvhtzxzqqjkmpb") == True
        assert check_character("xxyxx") == True
        assert check_double_pair("aabaa") == True
        assert check_double_pair("aaa") == False  # overlap

    def test_repeat_letter(self):
        assert check_contains_repeated_letter("aaa") == True
        assert check_contains_repeated_letter("abcdefeghi") == True
        assert check_contains_repeated_letter("efe") == True
        assert check_contains_repeated_letter("mm") == False
