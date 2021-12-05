from part1 import read_bingo_game, check_number, has_bingo, play_bingo

def find_last_winning_board(boards,random_numbers):
    while len(boards) > 1:
        number = random_numbers.pop(0)
        boards = [board for board in boards if not has_bingo(check_number(board,number))]
    # after finding last remaining bingo board, we need to continute to play until complete
    return play_bingo(boards,random_numbers)


def solve_puzzle(puzzle_input):
    boards,random_numbers = read_bingo_game(puzzle_input)

    board,number = find_last_winning_board(boards,random_numbers)
    board_total = sum(sum(_ for _ in row if _ >= 0) for row in board)

    return board_total*number

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))