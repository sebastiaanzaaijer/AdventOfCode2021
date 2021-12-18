from dataclasses import dataclass

INIT_RISK = 999999999999

@dataclass
class Cell:
    risk: int
    min_risk: int = INIT_RISK
    previous: tuple = None

def neighbour_generator(nx,ny):
    def neighbours(node):
        return 
    return neighbours

def solve_puzzle(puzzle_input):
    cavern = {}
    lines = puzzle_input.splitlines(False)
    for j in range(5):
        for y,l in enumerate(lines):
            for i in range(5):
                for x,_ in enumerate(l):
                    cavern[(len(l)*i+x,len(lines)*j+y)] = Cell((int(_)-1+(i+j))%9+1)
    cavern[(0,0)].min_risk = 0
    maxx = max(_[0] for _ in cavern.keys())
    maxy = max(_[1] for _ in cavern.keys())

    unvisited = set([(0,0)])
    visited = set([(0,0)])
    while unvisited:
        node = sorted(unvisited, key=lambda n: cavern[n].min_risk)[0]
        nns = set((max(0,min(node[0]+o[0],maxx)),max(0,min(node[1]+o[1],maxy))) for o in ((1,0),(0,1),(-1,0),(0,-1))) - visited
        unvisited.update(nns)
        for nn in nns:
            if cavern[node].min_risk+cavern[nn].risk < cavern[nn].min_risk:
                cavern[nn].min_risk = cavern[node].min_risk+cavern[nn].risk
                cavern[nn].previous = node
        unvisited.remove(node)
        visited.add(node)

    return cavern[(maxx,maxy)].min_risk


if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))