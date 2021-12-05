from collections import defaultdict, namedtuple

Point = namedtuple('Point', 'x y')
LineSegment = namedtuple('LineSegment', 'start end')

def solve_puzzle(puzzle_input):
    def extract_coordinates(line):
        return LineSegment(*(Point(*map(int,_.split(','))) for _ in line.split(' -> ')))

    line_segments = [extract_coordinates(_) for _ in puzzle_input.splitlines(False)]

    ocean_floor = defaultdict(int)

    for segment in line_segments:
        if segment.start.x == segment.end.x: # vertical line
            for y in range(min(segment.start.y,segment.end.y),max(segment.start.y,segment.end.y)+1):
                ocean_floor[Point(segment.start.x,y)] += 1
        elif segment.start.y == segment.end.y: # horizontal line
            for x in range(min(segment.start.x,segment.end.x),max(segment.start.x,segment.end.x)+1):
                ocean_floor[Point(x,segment.start.y)] += 1
                
    return sum(_ >= 2 for _ in ocean_floor.values())

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))