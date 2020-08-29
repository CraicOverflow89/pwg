from pwg import PasswordGenerator
import pytest, re


class TestPWG:
    def test_character_length(self):
        """
        Tests that generated password has default length of fifteen characters
        """
        assert 15 == len(PasswordGenerator().create())

    def test_contains_lowercase(self):
        """
        Tests that generated password contains an lowercase character
        """
        assert re.search("[a-z]", PasswordGenerator().create())

    def test_contains_numeric(self):
        """
        Tests that generated password contains a numeric character
        """
        assert re.search("[0-9]", PasswordGenerator().create())

    def test_contains_special(self):
        """
        Tests that generated password contains a special character from set
        """
        assert re.search("[!#$%&]", PasswordGenerator().create())

    def test_contains_uppercase(self):
        """
        Tests that generated password contains an uppercase character
        """
        assert re.search("[A-Z]", PasswordGenerator().create())
