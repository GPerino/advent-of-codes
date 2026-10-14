from unittest import TestCase

from main import check_character, check_double_letter, check_vowels_in_line, check_not_contains_prohibited_string


class Test(TestCase):

    def test_naughty_string(self):
        assert check_character("qjhvhtzxzqqjkmpb") == True  # pair appears twice + repeats letter
        assert check_character("xxyxx") == True  # corresponding twice rules
        assert check_character("uurcxstgmygtbstg") == False  # one pair only
        assert check_character("ieodomkazucvgmuy") == False  # no repeated # letter

    def test_must_contains_double_letter(self):
        assert check_double_letter("ddertyuiop") == True  # start of string
        assert check_double_letter("adeztrryid") == True  # middle of string
        assert check_double_letter("adeaeaeadd") == True  # end of string
        assert check_double_letter("dad") == False # same letter in start & end of string
        assert check_double_letter("dd") == True
        assert check_double_letter("aaa") == True
        assert check_double_letter("ad") == False
        assert check_double_letter("ab") == False
        assert check_double_letter("yy") == True
        assert check_double_letter("aa") == True

    def test_three_vowels(self):
        assert check_vowels_in_line("aiy") == False
        assert check_vowels_in_line("aaa") == True
        assert check_vowels_in_line("ababa") == True
        assert check_vowels_in_line("aeiou") == True
        assert check_vowels_in_line("xazegov") == True

    def test_prohibited_strings(self):
        assert check_not_contains_prohibited_string("ce") == True
        assert check_not_contains_prohibited_string("mf") == True
        assert check_not_contains_prohibited_string("ze") == True
        assert check_not_contains_prohibited_string("ab") == False
        assert check_not_contains_prohibited_string("cd") == False
        assert check_not_contains_prohibited_string("pq") == False
        assert check_not_contains_prohibited_string("xy") == False
