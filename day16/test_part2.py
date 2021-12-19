import unittest

from .part2 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input1(self):
        example_input = "C200B40A82"
        self.assertEqual(solve_puzzle(example_input),3)

    def test_example_input2(self):
        example_input = "04005AC33890"
        self.assertEqual(solve_puzzle(example_input),54)

    def test_example_inpu3(self):
        example_input = "880086C3E88112"
        self.assertEqual(solve_puzzle(example_input),7)

    def test_example_input4(self):
        example_input = "CE00C43D881120"
        self.assertEqual(solve_puzzle(example_input),9)

    def test_example_input5(self):
        example_input = "D8005AC2A8F0"
        self.assertEqual(solve_puzzle(example_input),1)

    def test_example_input6(self):
        example_input = "F600BC2D8F"
        self.assertEqual(solve_puzzle(example_input),0)

    def test_example_input7(self):
        example_input = "9C005AC2F8F0"
        self.assertEqual(solve_puzzle(example_input),0)

    def test_example_input7(self):
        example_input = "9C0141080250320F1802104A08"
        self.assertEqual(solve_puzzle(example_input),1)
