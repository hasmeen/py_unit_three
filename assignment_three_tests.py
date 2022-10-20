import string
import assignment_three
import unittest
from unittest.mock import Mock


class MyTestCase(unittest.TestCase):
    def test_get_side_length(self):
        """This test passed"""
        with unittest.mock.patch('builtins.input', return_value="100"):
            assert type(assignment_three.get_side_length()) == float


    def test_get_petal_color(self):
        """This test failed with AssertionError in assert type(assignment_three.get_petal_color()) == string"""
        with unittest.mock.patch('builtins.input', return_value="blue"):
            assert type(assignment_three.get_petal_color()) == string

    def test_get_center_color(self):
        """This test failed with AssertionError in assert type(assignment_three.get_center_color()) == string"""
        with unittest.mock.patch('builtins.input', return_value="red"):
            assert type(assignment_three.get_center_color()) == string


if __name__ == '__main__':
    unittest.main()
