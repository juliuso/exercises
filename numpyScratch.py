#!/usr/bin/env python
import os
import numpy as np

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


if __name__ == "__main__":
    p = np.array(puzzle)
    puzzle_groups = []

    for split_row_thirds in np.vsplit(p, 3):
        for split_col_thirds in np.hsplit(split_row_thirds, 3):
            puzzle_groups.append(split_col_thirds.flatten())

    print(puzzle_groups)

"""
[array([5, 3, 0, 6, 0, 0, 0, 9, 8]),
array([0, 7, 0, 1, 9, 5, 0, 0, 0]),
array([0, 0, 0, 0, 0, 0, 0, 6, 0]),
array([8, 0, 0, 4, 0, 0, 7, 0, 0]),
array([0, 6, 0, 8, 0, 3, 0, 2, 0]),
array([0, 0, 3, 0, 0, 1, 0, 0, 6]),
array([0, 6, 0, 0, 0, 0, 0, 0, 0]),
array([0, 0, 0, 4, 1, 9, 0, 8, 0]),
array([2, 8, 0, 0, 0, 5, 0, 7, 9])]
"""

