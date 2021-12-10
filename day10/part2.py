def parse_line(l):
    inv = {'(':')','[':']','{':'}','<':'>',}  
    opened = []
    for c in l:
        if c in '([{<':
            opened.append(c)
        if c in ')]}>':
            if inv[opened.pop()] != c:
                return
    return [inv[_] for _ in reversed(opened)]

def calc_score(compl):
    points = {')':1,']':2,'}':3,'>':4}
    total = 0
    for c in compl:
        total = 5*total+points[c]
    return total



def solve_puzzle(puzzle_input):
    points = {')':1,']':2,'}':3,'>':4}
    compl = (parse_line(l) for l in puzzle_input.splitlines(False) if parse_line(l))
    scores = [calc_score(c) for c in compl]
    return sorted(scores)[len(scores)//2]

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))