from math import prod

def expand_basin(point,height_map,points_in_basin=None):
    if not points_in_basin:
        points_in_basin = set([point])
    for dx in (-1,1):
        p = point[0]+dx,point[1]
        if height_map[p[0]][p[1]] < 9 and p not in points_in_basin: 
            points_in_basin.add(p)
            expand_basin(p,height_map,points_in_basin)
    for dy in (-1,1):
        p = point[0],point[1]+dy
        if height_map[p[0]][p[1]] < 9 and p not in points_in_basin: 
            points_in_basin.add(p)
            expand_basin(p,height_map,points_in_basin)

    return len(points_in_basin)


def solve_puzzle(puzzle_input):
    height_map = [[int(_) for _ in l]+[9] for l in puzzle_input.splitlines(False)]
    height_map.append([9]*len(height_map[0]))
    low_points = []
    for i in range(len(height_map)-1):
        for j in range(len(height_map[0])-1):
            if height_map[i][j] < min(height_map[i+1][j],height_map[i-1][j],height_map[i][j-1],height_map[i][j+1]):
                low_points.append((i,j))
    return prod(sorted(expand_basin(point,height_map) for point in low_points)[-3:])

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))