#!/usr/bin/python3
"""
this will n puzzle solver prog
"""


import sys


def init_board(n):
    """set n x n init."""
    board = []
    [board.append([]) for l in range(n)]
    [row.append(' ') for l in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """this will get cpy for the chessface."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """this func will get solved lst for the board."""
    solution = []
    for k in range(len(board)):
        for lp in range(len(board)):
            if board[k][lp] == "Q":
                solution.append([k, lp])
                break
    return (solution)


def out_put(board, row, col):
    """this func will ret the point in chess.

    Args:
        empset: env playing.
        row: brev row.
        col: brev col.
    """
    # out_put_ret forward
    for lp in range(col + 1, len(board)):
        board[row][lp] = "x"
    # backwards out_put_ret
    for lp in range(col - 1, -1, -1):
        board[row][lp] = "x"
    # below out_put_ret
    for k in range(row + 1, len(board)):
        board[k][col] = "x"
    # above out_put_ret
    for k in range(row - 1, -1, -1):
        board[k][col] = "x"
    # down -> right out_put_ret
    lp = col + 1
    for k in range(row + 1, len(board)):
        if lp >= len(board):
            break
        board[k][lp] = "x"
        lp += 1
    # diagonally up <- left out_put_ret
    lp = col - 1
    for k in range(row - 1, -1, -1):
        if lp < 0:
            break
        board[k][lp]
        lp -= 1
    # out_put_ret diagonally up to the right
    lp = col + 1
    for k in range(row - 1, -1, -1):
        if lp >= len(board):
            break
        board[k][lp] = "x"
        lp += 1
    # diagonally down -< left out_put_ret
    lp = col - 1
    for k in range(row + 1, len(board)):
        if lp < 0:
            break
        board[k][lp] = "x"
        lp -= 1


def the_solver_func(board, row, queens, solutions):
    """this func will be the solver func.

    Args:
        empset: inst board.
        row: inst row.
        queens: inst num of queens.
        solutions : z lst.
    Returns:
        this will ret the game z
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for lp in range(len(board)):
        if board[row][lp] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][lp] = "Q"
            out_put(tmp_board, row, lp)
            solutions = the_solver_func(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = the_solver_func(board, 0, 0, [])
    for z in solutions:
        print(z)
