import unittest

from .part2 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = "3,4,3,1,2"
        self.assertEqual(solve_puzzle(example_input),26984457539)

