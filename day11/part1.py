def step(grid):
    offsets = (
        (-1,-1),
        (0,-1),
        (1,-1),
        (-1,0),
        (1,0),
        (-1,1),
        (0,1),
        (1,1),
    )
    for i in range(len(grid)-1):
        for j in range(len(grid[0])-1):
            grid[i][j] += 1
    while max((max(_) for _ in grid)) > 9:
        for i in range(len(grid)-1):
            for j in range(len(grid[0])-1):
                if grid[i][j] > 9:
                    grid[i][j] = 0
                    for o in offsets:
                        if grid[i+o[0]][j+o[1]] > 0:
                            grid[i+o[0]][j+o[1]] += 1
    return grid

def print_grid(grid):
    return '\n'.join(''.join(str(_) for _ in row[:-1]) for row in grid[:-1])

def solve_puzzle(puzzle_input):
    grid = [list(map(int,_))+[-1] for _ in puzzle_input.splitlines(False)]
    grid.append([-1]*len(grid[0]))
    flashes = 0
    for i in range(100):
        grid = step(grid)
        flashes += sum(_.count(0) for _ in grid)
    return flashes

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))