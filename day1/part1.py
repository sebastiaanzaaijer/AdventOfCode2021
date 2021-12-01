def solve_puzzle(puzzle_input):
    lines = puzzle_input.splitlines(keepends=False)
    return sum(int(b)>int(a) for a,b in zip(lines[:-1],lines[1:]))

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))