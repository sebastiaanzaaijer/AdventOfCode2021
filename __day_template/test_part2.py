import unittest

from .part2 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = ""
        self.assertEqual(solve_puzzle(example_input),"")

