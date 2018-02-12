
from __future__ import print_function

import numpy as np
import time
import unittest

from test.boards import ALL_BOARDS, SOLVABLE, is_complete
from yass.numpy_solver import solve


class TestNumpySolver(unittest.TestCase):

    def test_validity(self):
        for test, solvable in zip(ALL_BOARDS, SOLVABLE):
            board = np.asarray(test)
            print(board)
            s = solve(board)
            print(s)
            print()
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
                s = solve(np.asarray(test))
                self.assertTrue(s is None or is_complete(s))
                print("Time (ms)", 1000 / repetitions * (time.time() - t))
        print("Total time (s)", time.time() - t0)