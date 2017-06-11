import unittest
from copy import copy

from sort import sort

INPUT = [49, 32, 74, 79, 43, 31, 81, 64, 8, 71]
OUTPUT = [8, 31, 32, 43, 49, 64, 71, 74, 79, 81]


class Generator:
    def __init__(self, assertions: unittest.TestCase):
        self.assertions = assertions

    def try_with(self, algorithm, input, expected):
        # given
        array = copy(input)
        # when
        algorithm(array)
        # then
        self.assertions.assertEqual(array, expected)


class TestSort(unittest.TestCase):
    def test_insertion(self):
        Generator(self).try_with(sort.insertion, INPUT, OUTPUT)

    def test_selection(self):
        Generator(self).try_with(sort.selection, INPUT, OUTPUT)

    def test_bubble(self):
        Generator(self).try_with(sort.bubble, INPUT, OUTPUT)

    def test_shell(self):
        Generator(self).try_with(sort.shell, INPUT, OUTPUT)
