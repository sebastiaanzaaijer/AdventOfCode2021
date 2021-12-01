import unittest

from .part2 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """199
200
208
210
200
207
240
269
260
263"""
        self.assertEqual(solve_puzzle(example_input),5)

