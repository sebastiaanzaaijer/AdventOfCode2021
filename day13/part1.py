def fold_paper(dots,fold):
    new_dots = set()
    if fold[0] == 'x':
        for dot in dots:
            if dot[0]<fold[1]:
                new_dots.add(dot)
            else:
                new_dots.add((fold[1]-(dot[0]-fold[1]),dot[1]))
    else:
        for dot in dots:
            if dot[1]<fold[1]:
                new_dots.add(dot)
            else:
                new_dots.add((dot[0],fold[1]-(dot[1]-fold[1])))        
    return new_dots

def print_paper(dots):
    size_x = max(dot[0] for dot in dots)
    size_y = max(dot[1] for dot in dots)
    printed = ""
    for y in range(size_y+1):
        for x in range(size_x+1):
            if (x,y) in dots:
                printed += '#'
            else:
                printed += '.'
        printed += '\n'
    return printed

def solve_puzzle(puzzle_input):
    lines = puzzle_input.splitlines(False)
    dots = set()
    while lines:
        line = lines.pop(0)
        if not line:
            break
        dots.add(tuple(map(int,line.split(','))))
    
    folds = []
    while lines:
        line = lines.pop(0)
        fold = line.split()[-1].split('=')
        fold[1] = int(fold[1])
        folds.append(fold)

    return len(fold_paper(dots,folds[0]))

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))