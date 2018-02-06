
from __future__ import print_function

import numpy as np
import time
import unittest

from solver import COMPLETE, ROWS, COLS, SQUARES, solve


a = [[0, 0, 0,  2, 0, 0,  0, 1, 0],
     [0, 9, 0,  0, 0, 0,  4, 0, 0],
     [8, 0, 6,  0, 0, 0,  0, 0, 0],

     [0, 7, 1,  0, 8, 4,  0, 9, 0],
     [0, 5, 0,  0, 0, 2,  3, 7, 0],
     [0, 0, 0,  0, 0, 0,  0, 0, 0],

     [0, 0, 0,  7, 1, 0,  0, 6, 4],
     [0, 2, 0,  0, 0, 5,  0, 0, 0],
     [3, 0, 0,  4, 0, 0,  0, 0, 9]]

b = [[0, 0, 5,  9, 6, 0,  0, 0, 7],
     [0, 0, 0,  0, 0, 0,  0, 5, 0],
     [0, 0, 2,  0, 0, 0,  4, 0, 9],

     [0, 0, 0,  0, 0, 0,  0, 4, 0],
     [2, 0, 0,  8, 0, 0,  9, 0, 0],
     [4, 0, 1,  0, 0, 0,  5, 0, 3],

     [3, 2, 9,  1, 0, 6,  0, 0, 0],
     [1, 0, 4,  0, 0, 0,  0, 3, 0],
     [0, 0, 0,  0, 8, 2,  0, 0, 0]]

c = [[0, 0, 0,  0, 0, 0,  0, 2, 0],
     [0, 8, 1,  0, 0, 6,  0, 0, 0],
     [0, 0, 0,  0, 0, 0,  4, 3, 0],

     [0, 0, 6,  0, 0, 1,  0, 9, 8],
     [0, 0, 0,  0, 0, 0,  0, 0, 0],
     [0, 0, 7,  0, 0, 0,  0, 6, 3],

     [0, 0, 3,  5, 6, 9,  2, 0, 7],
     [5, 7, 9,  2, 0, 0,  0, 0, 0],
     [0, 0, 0,  0, 0, 7,  0, 0, 0]]

z = [[0, 0, 0,  0, 0, 0,  0, 0, 0],
     [0, 0, 0,  0, 0, 0,  0, 0, 0],
     [0, 0, 0,  0, 0, 0,  0, 0, 0],

     [0, 0, 0,  0, 0, 0,  0, 0, 0],
     [0, 0, 0,  0, 0, 0,  0, 0, 0],
     [0, 0, 0,  0, 0, 0,  0, 0, 0],

     [0, 0, 0,  0, 0, 0,  0, 0, 0],
     [0, 0, 0,  0, 0, 0,  0, 0, 0],
     [0, 0, 0,  0, 0, 0,  0, 0, 0]]

vdsp1 = [
    [4, 0, 0,  5, 0, 0,  0, 0, 6],
    [0, 0, 0,  0, 0, 0,  0, 2, 0],
    [1, 0, 9,  0, 0, 7,  0, 5, 0],

    [0, 0, 0,  7, 0, 0,  0, 0, 0],
    [0, 4, 0,  0, 0, 0,  0, 0, 0],
    [7, 0, 6,  0, 0, 3,  1, 0, 8],

    [0, 0, 0,  2, 0, 0,  0, 0, 5],
    [0, 8, 0,  0, 9, 0,  7, 0, 0],
    [0, 0, 3,  0, 8, 0,  0, 0, 4]
]

hardest = [
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 1, 0,  6, 2, 0,  0, 9, 0],
    [0, 0, 2,  0, 0, 9,  3, 1, 0],

    [0, 0, 4,  0, 0, 6,  0, 8, 0],
    [0, 0, 8,  7, 0, 2,  1, 0, 0],
    [0, 3, 0,  8, 0, 0,  5, 0, 0],

    [0, 6, 9,  1, 0, 0,  4, 0, 0],
    [0, 8, 0,  0, 7, 3,  0, 5, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0]
]

ones = [
    [1, 1, 1,  1, 1, 1,  1, 1, 1],
    [1, 1, 1,  1, 1, 1,  1, 1, 1],
    [1, 1, 1,  1, 1, 1,  1, 1, 1],

    [1, 1, 1,  1, 1, 1,  1, 1, 1],
    [1, 1, 1,  1, 1, 1,  1, 1, 1],
    [1, 1, 1,  1, 1, 1,  1, 1, 1],

    [1, 1, 1,  1, 1, 1,  1, 1, 1],
    [1, 1, 1,  1, 1, 1,  1, 1, 1],
    [1, 1, 1,  1, 1, 1,  1, 1, 1]
]


ALL_BOARDS = (a, b, c, z, vdsp1, hardest, ones)
EXPECTED = (True, True, True, True, True, True, False)


def is_complete(board):

    board = np.asarray(board)

    return board.all() and \
           all(set(board[r,:]) == COMPLETE for r in ROWS) and \
           all(set(board[:,c]) == COMPLETE for c in COLS) and \
           all(all(set(board[r:r + 3, c:c + 3].flat) == COMPLETE for c in SQUARES) for r in SQUARES)


class TestSolver2(unittest.TestCase):

    def test_validity(self):
        for board, expected in zip(ALL_BOARDS, EXPECTED):
            print(board)
            s = solve(board)
            print(s)
            print()
            if expected:
                self.assertTrue(s is not None and is_complete(s))
            else:
                self.assertIsNone(s)

    def test_speed(self):
        t0 = time.time()
        for test in ALL_BOARDS:
            repetitions = 10
            for i in range(repetitions):
                t = time.time()
                s = solve(test)
                self.assertTrue(s is None or is_complete(s))
                print("Time (ms)", 1000 / repetitions * (time.time() - t))
        print("Total time (s)", time.time() - t0)