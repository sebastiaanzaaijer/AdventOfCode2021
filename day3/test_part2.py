import unittest

from .part2 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
        self.assertEqual(solve_puzzle(example_input),230)
