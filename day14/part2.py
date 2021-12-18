from collections import defaultdict, Counter
import time
def grow_polymer(pairs,insertions):
    new_pairs = defaultdict(int)
    for pair in pairs:
        insertion = insertions[pair]
        new_pairs[pair[0]+insertion] += pairs[pair]
        new_pairs[insertion+pair[1]] += pairs[pair]
    return new_pairs


def solve_puzzle(puzzle_input):
    lines = puzzle_input.splitlines(False)
    polymer = lines[0]
    pairs = defaultdict(int)
    for i in range(len(polymer)-1):
        pairs[polymer[i:i+2]] += 1

    insertions = defaultdict(str)
    for l in lines[2:]:
        pair, insert = l.split(' -> ')
        insertions[pair] = insert
    
    for i in range(40):
        pairs = grow_polymer(pairs,insertions)
    element_counts = defaultdict(int)
    for k,v in pairs.items():
        element_counts[k[0]] += v//2
        element_counts[k[1]] += v//2

    return max(element_counts.values())-min(element_counts.values())

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))