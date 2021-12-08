from collections import Counter

def solve_puzzle(puzzle_input):
    crabs = Counter(map(int,puzzle_input.split(',')))
    pmin = min(crabs)
    pmax = max(crabs)

    min_fuel = 9999999999999999

    for i in range(pmin,pmax):
        fuel = sum(abs((pos-i)**2+abs(pos-i))//2*crabs[pos] for pos in crabs)
        min_fuel = min(fuel,min_fuel)

    return min_fuel

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))