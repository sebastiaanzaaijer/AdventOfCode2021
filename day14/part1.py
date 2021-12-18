from collections import defaultdict, Counter

def grow_polymer(polymer,insertions):
    new_polymer = ''
    for i in range(len(polymer)-1):
        new_polymer += polymer[i]
        new_polymer += insertions[polymer[i:i+2]]
    new_polymer += polymer[-1]
    return new_polymer


def solve_puzzle(puzzle_input):
    lines = puzzle_input.splitlines(False)
    polymer = lines[0]
    insertions = defaultdict(str)
    for l in lines[2:]:
        pair, insert = l.split(' -> ')
        insertions[pair] = insert
    for i in range(10):
        polymer = grow_polymer(polymer,insertions)
    element_counts = Counter(polymer)
    return max(element_counts.values())-min(element_counts.values())

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))