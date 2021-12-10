def parse_line(l):
    inv = {'(':')','[':']','{':'}','<':'>',}  
    opened = []
    for c in l:
        if c in '([{<':
            opened.append(c)
        if c in ')]}>':
            if inv[opened.pop()] != c:
                return c


def solve_puzzle(puzzle_input):
    points = {')':3,']':57,'}':1197,'>':25137,None:0}
    return sum(points[parse_line(l)] for l in puzzle_input.splitlines(False))

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))