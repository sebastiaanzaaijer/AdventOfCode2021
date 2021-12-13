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
    all_routes = set()
    for node in network:
        if not node in ('start','end') and node[0].islower():
            modified_network = {k:v.copy() for k,v in network.items()}
            modified_network['duplicate'] = modified_network[node].copy()
            for n,d in modified_network.items():
                if node in d:
                    d.add('duplicate')
            all_routes.update(','.join(_).replace('duplicate',node) for _ in walk(modified_network))

    # for route in sorted(all_routes):
    #     print(route)
    # print(len(all_routes))
    return len(all_routes)

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))