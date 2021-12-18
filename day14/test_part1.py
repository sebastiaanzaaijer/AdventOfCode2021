import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
        self.assertEqual(solve_puzzle(example_input),1588)
