def solve_puzzle(puzzle_input):
    lines = puzzle_input.splitlines()
    gamma = int("".join((str(int(sum(map(int,_))>len(lines)//2)) for _ in zip(*lines))),2)
    epsilon  = int("".join((str(int(sum(map(int,_))<len(lines)//2)) for _ in zip(*lines))),2)
    return gamma*epsilon

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))