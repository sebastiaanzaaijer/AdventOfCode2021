from os import read


def read_bingo_game(puzzle_input):
    lines = puzzle_input.splitlines(False)
    random_numbers = [int(_) for _ in lines.pop(0).split(',')]

    boards = []
    while lines:
        lines.pop(0)
        board = []
        for i in range(5):
            board.append([int(_) for _ in lines.pop(0).split()])
        boards.append(board)
    return boards,random_numbers

def has_bingo(board):
    for row in board:
        if sum(row) == -5:
            return True
    for col in zip(*board):
        if sum(col) == -5:
            return True        
    return False

def check_number(board,number):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                board[i][j] = -1
    return board

def play_bingo(boards,random_numbers):
    while True:
        number = random_numbers.pop(0)
        for board in boards:
            if has_bingo(check_number(board,number)): 
                return board,number


def solve_puzzle(puzzle_input):    
    boards,random_numbers = read_bingo_game(puzzle_input)

    board,number = play_bingo(boards,random_numbers)
    board_total = sum(sum(_ for _ in row if _ >= 0) for row in board)

    return board_total*number

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))