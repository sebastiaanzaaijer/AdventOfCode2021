import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""
        self.assertEqual(solve_puzzle(example_input),15)
