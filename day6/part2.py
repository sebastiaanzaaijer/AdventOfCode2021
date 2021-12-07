from collections import Counter, defaultdict

def spawn(population):
    new_population = defaultdict(int)
    for age in range(7,-1,-1):
        new_population[age] = population[age+1]
    new_population[8] = population[0]
    new_population[6] += population[0]
    return new_population

def solve_puzzle(puzzle_input):
    population = defaultdict(int,Counter(map(int,puzzle_input.split(','))))
    for age in range(8):
        if not age in population:
            population[age] = 0
    for i in range(256):
        population = spawn(population)

    return sum(population.values())

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))