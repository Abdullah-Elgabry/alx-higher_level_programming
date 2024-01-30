#!/usr/bin/python3
"""
this will n puzzle solver prog
"""


import sys


def init_board(n):
    """set n x n init."""
    empset = []
    [empset.append([]) for s in range(n)]
    [row.append(' ') for s in range(n) for row in empset]
    return (empset)


def get_solution(empset):
    """this func will get sloved chess rep list."""
    emppsd = []
    for solx in range(len(empset)):
        for sc in range(len(empset)):
            if empset[solx][sc] == "Q":
                emppsd.append([solx, sc])
                break
    return (emppsd)


def board_deepcopy(empset):
    """this will get cpy for the chessface."""
    if isinstance(empset, list):
        return list(map(board_deepcopy, empset))
    return (empset)


def out_put(empset, row, col):
    """this func will ret the point in chess.

    Args:
        empset: env playing.
        row: brev row.
        col: brev col.
    """
    for sc in range(col + 1, len(empset)):
        empset[row][sc] = "x"

    for sc in range(col - 1, -1, -1):
        empset[row][sc] = "x"

    for solx in range(row + 1, len(empset)):
        empset[solx][col] = "x"

    for solx in range(row - 1, -1, -1):
        empset[solx][col] = "x"

    sc = col + 1
    for solx in range(row + 1, len(empset)):
        if sc >= len(empset):
            break
        empset[solx][sc] = "x"
        sc += 1

    sc = col - 1
    for solx in range(row - 1, -1, -1):
        if sc < 0:
            break
        empset[solx][sc]
        sc -= 1

    sc = col + 1
    for solx in range(row - 1, -1, -1):
        if sc >= len(empset):
            break
        empset[solx][sc] = "x"
        sc += 1

    sc = col - 1
    for solx in range(row + 1, len(empset)):
        if sc < 0:
            break
        empset[solx][sc] = "x"
        sc -= 1


def the_solver(empset, row, queens, solutions):
    """this func will be the solver func.

    Args:
        empset: inst board.
        row: inst row.
        queens: inst num of queens.
        solutions : z lst.
    Returns:
        this will ret the game z
    """
    if queens == len(empset):
        solutions.append(get_solution(empset))
        return (solutions)

    for sc in range(len(empset)):
        if empset[row][sc] == " ":
            tmp_board = board_deepcopy(empset)
            tmp_board[row][sc] = "Q"
            out_put(tmp_board, row, sc)
            solutions = the_solver(tmp_board, row + 1,
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

    empset = init_board(int(sys.argv[1]))
    solutions = the_solver(empset, 0, 0, [])
    for psd in solutions:
        print(psd)
