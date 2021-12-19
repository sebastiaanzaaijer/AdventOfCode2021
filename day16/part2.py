from math import prod
from itertools import chain

global indent

indent = 0
def gen_operator(operant):
    def f(packet):
        operant_result = operator(packet)
        return operant(operant_result)
    f.operant = operant.__name__
    return f


def operator(packet):
    global indent
    indent += 1
    length_bit = int(packet.pop(0),2)
    results = []
    if length_bit == 0:
        n_packet_bits = int(''.join(packet.pop(0) for i in range(15)),2)
        packet_bits = [packet.pop(0) for i in range(n_packet_bits)]
        while packet_bits:
            results.append(packet_decoder(packet_bits))
    else:
        n_packets = int(''.join(packet.pop(0) for i in range(11)),2)
        for _ in range(n_packets):
            results.append(packet_decoder(packet))
    return results

def litteral_value(packet):
    global indent
    indent -= 1
    values = []
    last = not int(packet.pop(0),2)
    while not last:
        values.extend(packet.pop(0) for i in range(4))
        last = not int(packet.pop(0),2)
    values.extend(packet.pop(0) for i in range(4))
    return int(''.join(values),2)


def gt(x):
    return int(x[0]>x[1])

def lt(x):
    return int(x[0]<x[1])

def eq(x):
    return int(x[0]==x[1])

dispatch = {
    0: gen_operator(sum),
    1: gen_operator(prod),
    2: gen_operator(min),
    3: gen_operator(max),
    4: litteral_value,
    5: gen_operator(gt),
    6: gen_operator(lt),
    7: gen_operator(eq),
}

def packet_decoder(packet):
    version = int(''.join(packet.pop(0) for i in range(3)),2)
    type_id = int(''.join(packet.pop(0) for i in range(3)),2)
    return dispatch.get(type_id)(packet)


def solve_puzzle(puzzle_input):
    as_binary = list(''.join('{:04b}'.format(int(_,16)) for _ in puzzle_input))
    return packet_decoder(as_binary)

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))
