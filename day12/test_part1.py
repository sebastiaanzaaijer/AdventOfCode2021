import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_simple_example_input(self):
        example_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
        self.assertEqual(solve_puzzle(example_input),10)

    def test_example_input(self):
        example_input = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
        self.assertEqual(solve_puzzle(example_input),19)

    def test_large_example_input(self):
        example_input = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""
        self.assertEqual(solve_puzzle(example_input),226)