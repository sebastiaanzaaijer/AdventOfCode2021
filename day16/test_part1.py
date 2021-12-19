import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input1(self):
        example_input = "D2FE28"
        self.assertEqual(solve_puzzle(example_input),6)

    def test_example_input2(self):
        example_input = "8A004A801A8002F478"
        self.assertEqual(solve_puzzle(example_input),16)

    def test_example_input3(self):
        example_input = "620080001611562C8802118E34"
        self.assertEqual(solve_puzzle(example_input),12)

    def test_example_input4(self):
        example_input = "C0015000016115A2E0802F182340"
        self.assertEqual(solve_puzzle(example_input),23)

    def test_example_input5(self):
        example_input = "A0016C880162017C3686B18A3D4780"
        self.assertEqual(solve_puzzle(example_input),31)

