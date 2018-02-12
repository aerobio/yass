
from __future__ import print_function

import time
import unittest

from test.boards import ALL_BOARDS, SOLVABLE, is_complete
from yass.solver import solve


def print_board(board):
    if board is None:
        print(board)
    else:
        for row in board:
            print(row)
        print()


class TestSolver(unittest.TestCase):

    def test_validity(self):
        for board, solvable in zip(ALL_BOARDS, SOLVABLE):
            print()
            print_board(board)
            s = solve(board)
            print_board(s)
            if solvable:
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