def is_unique_digit(sequence):
    return len(sequence) in (2,3,4,7)

def solve_puzzle(puzzle_input):
    return sum(sum(map(is_unique_digit,l.split(' | ')[1].split())) for l in puzzle_input.splitlines(False))

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))