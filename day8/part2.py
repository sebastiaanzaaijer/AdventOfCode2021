def solve_puzzle(puzzle_input):
    total = 0
    for line in puzzle_input.splitlines(False):
        observations, digits = line.split(' | ')
        observations = [''.join(sorted(_)) for _ in observations.split()]
        digits = [''.join(sorted(_)) for _ in digits.split()]
        known_digits = [
            None, #0
            [o for o in observations if len(o)==2][0], #1
            None, #2
            None, #3
            [o for o in observations if len(o)==4][0], #4
            None, #5
            None, #6
            [o for o in observations if len(o)==3][0], #7
            [o for o in observations if len(o)==7][0], #8
            None #9
        ]
        known_digits[2] = [o for o in observations if len(o) == 5 and len(set(o)-set(known_digits[4]))==3][0]
        known_digits[9] = [o for o in observations if len(o) == 6 and len(set(o) - set(known_digits[4]))==2][0]
        # wire_map = { elementA: "A"}
        element_d = ((set(known_digits[4]) & set(known_digits[2]) & set(known_digits[8]) & set(known_digits[9]))-set(known_digits[1])).pop()
        known_digits[0] = [o for o in observations if len(o) == 6 and not element_d in o][0]
        known_digits[6] = [o for o in observations if len(o) == 6 and not o in [known_digits[0],known_digits[9]]][0]
        known_digits[5] = [o for o in observations if len(o) == 5 and len(set(o)-set(known_digits[6])) == 0][0]
        known_digits[3] = [o for o in observations if len(o) == 5 and not o in [known_digits[2],known_digits[5]]][0]
        known_digits_inv = {v: k for k, v in enumerate(known_digits)}
        total += sum(10**(3-v)*known_digits_inv[d] for v,d in enumerate(digits,0))
    return total

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))