

def solve_puzzle(puzzle_input):
    def number_counts(lst,level):
        ones = sum(int(_[level]) for _ in lst)
        zeros = len(lst)-ones
        return zeros,ones 

    O2gen = puzzle_input.splitlines()
    CO2scrub = O2gen[:]
    for i in range(len(O2gen[0])):
        if len(O2gen) > 1:
            zeros,ones = number_counts(O2gen,i)
            if ones >= zeros:
                O2gen = list(filter(lambda x: x[i] == '1',O2gen))
            else:
                O2gen = list(filter(lambda x: x[i] == '0',O2gen))
        
        if len(CO2scrub) > 1:
            zeros,ones = number_counts(CO2scrub,i)
            if ones < zeros:
                CO2scrub = list(filter(lambda x: x[i] == '1',CO2scrub))
            else:
                CO2scrub = list(filter(lambda x: x[i] == '0',CO2scrub))
    return int(O2gen[0],2)*int(CO2scrub[0],2)

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))