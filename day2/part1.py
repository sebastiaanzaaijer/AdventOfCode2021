def solve_puzzle(puzzle_input):
    position = [0,0]
    for instruction in puzzle_input.splitlines():
        direction,step = instruction.split()
        step = int(step)
        if direction == "up":
            position[1] -= step
        if direction == "down":
            position[1] += step
        if direction == "forward":
            position[0] += step
    return position[0]*position[1]

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))