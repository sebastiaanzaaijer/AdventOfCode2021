from collections import defaultdict

def walk(network, node=None, routes=None, visits=None):
    if routes is None:
        routes = []
    if node is None:
        node = 'start'
    if visits is None:
        visits = []

    visits.append(node)
    if visits[-1] == 'end':
        routes.append(visits)
        return routes

    visited = set(_ for _ in visits if _[0].islower())
    for next in network[node]-visited:
        walk(network, node=next, routes=routes, visits=visits.copy())
    return routes


def solve_puzzle(puzzle_input):
    network = defaultdict(set)
    for l in puzzle_input.splitlines(False):
        node1, node2 = l.split('-')
        network[node1].add(node2)
        network[node2].add(node1)

    routes = walk(network)
    return len(routes)

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))