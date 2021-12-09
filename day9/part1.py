def solve_puzzle(puzzle_input):
    height_map = [[int(_) for _ in l]+[9] for l in puzzle_input.splitlines(False)]
    height_map.append([9]*len(height_map[0]))
    risk = 0
    for i in range(len(height_map)-1):
        for j in range(len(height_map[0])-1):
            if height_map[i][j] < min(height_map[i+1][j],height_map[i-1][j],height_map[i][j-1],height_map[i][j+1]):
                risk += height_map[i][j]+1
    return risk

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))