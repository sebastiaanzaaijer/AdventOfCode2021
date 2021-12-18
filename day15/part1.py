from dataclasses import dataclass

INIT_RISK = 999999999999

@dataclass
class Cell:
    risk: int
    min_risk: int = INIT_RISK
    previous: tuple = None

def solve_puzzle(puzzle_input):
    cavern = {}
    for y,l in enumerate(puzzle_input.splitlines(False)):
        for x,_ in enumerate(l):
            cavern[(x,y)] = Cell(int(_))
    cavern[(0,0)].min_risk = 0
    maxx = max(_[0] for _ in cavern.keys())
    maxy = max(_[1] for _ in cavern.keys())

    unvisited = set(cavern.keys())
    visited = set([(0,0)])
    while unvisited:
        node = sorted(unvisited, key=lambda n: cavern[n].min_risk)[0]
        nns = set((max(0,min(node[0]+o[0],maxx)),max(0,min(node[1]+o[1],maxy))) for o in ((1,0),(0,1),(-1,0),(0,-1))) - visited
        for nn in nns:
            if cavern[node].min_risk+cavern[nn].risk < cavern[nn].min_risk:
                cavern[nn].min_risk = cavern[node].min_risk+cavern[nn].risk
                cavern[nn].previous = node
        unvisited.remove(node)
        visited.add(node)

    visited = []
    node = maxx,maxy
    while node != (0,0):
        visited.append(node)
        node = cavern[node].previous
    for j in range(maxy+1):
        for i in range(maxx+1):
            if (i,j) in visited:
                print('#',end='')
            else:
                print('.',end='')
        print()
    return cavern[(maxx,maxy)].min_risk


if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))