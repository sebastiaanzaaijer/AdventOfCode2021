def solve_puzzle(puzzle_input):
    values = [int(_) for _ in puzzle_input.splitlines(keepends=False)]
    
    return sum(sum(values[i:i+3])<sum(values[i+1:i+4]) for i in range(len(values)-2))

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))