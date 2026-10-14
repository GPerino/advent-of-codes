from unittest import TestCase

from main import check_character, check_double_letter, check_vowels_in_line, check_contains_prohibited_string


class Test(TestCase):

    def test_naughty_string(self):
        assert check_character("jchzalrnumimnmhp") == False  # no double letter
        assert check_character("haegwjzuvuyypxyu") == False  # contains "xy"
        assert check_character("dvszwmarrgswjxmb") == False  # one vowel

    def test_must_contains_double_letter(self):
        assert check_double_letter("dd") == True
        assert check_double_letter("de") == False

    def test_three_vowels(self):
        assert check_vowels_in_line("aiy") == False
        assert check_vowels_in_line("aaa") == True
        assert check_vowels_in_line("aeiou") == True
        assert check_vowels_in_line("xazegov") == True

    def test_prohibited_strings(self):
        assert check_contains_prohibited_string("ab") == False
        assert check_contains_prohibited_string("cd") == False
        assert check_contains_prohibited_string("pq") == False
        assert check_contains_prohibited_string("xy") == False
