def operator(packet,versions):
    length_bit = int(packet.pop(0),2)
    if length_bit == 0:
        n_packet_bits = int(''.join(packet.pop(0) for i in range(15)),2)
        packet_bits = [packet.pop(0) for i in range(n_packet_bits)]
        while packet_bits:
            packet_decoder(packet_bits,versions)
    else:
        n_packets = int(''.join(packet.pop(0) for i in range(11)),2)
        for _ in range(n_packets):
            packet_decoder(packet,versions)

def litteral_value(packet,versions):
    values = []
    last = not int(packet.pop(0),2)
    while not last:
        values.append(int(''.join(packet.pop(0) for i in range(4)),2))
        last = not int(packet.pop(0),2)
    values.append(int(''.join(packet.pop(0) for i in range(4)),2))


dispatch = {
    4: litteral_value,
}

def packet_decoder(packet,versions=None):
    if not versions:
        versions = []
    versions.append(int(''.join(packet.pop(0) for i in range(3)),2))
    type_id = int(''.join(packet.pop(0) for i in range(3)),2)
    dispatch.get(type_id,operator)(packet, versions)
    return versions


def solve_puzzle(puzzle_input):
    as_binary = list(''.join('{:04b}'.format(int(_,16)) for _ in puzzle_input))
    return sum(packet_decoder(as_binary))

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))