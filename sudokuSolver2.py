#!/usr/bin/env python
import os
import numpy as np

puzzle = np.array(
    [
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
)
# Bring this into driver() after finished.
deck = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def get_row_complement(row, col):
    return deck - set(puzzle[row]) - {0}


def get_column_complement(row, col):
    return deck - set((puzzle.T)[col]) - {0}


def get_group_complement(row, col):
    # Pending implementation.
    _ = []

    for split_row_thirds in np.vsplit(puzzle, 3):
        for split_col_thirds in np.hsplit(split_row_thirds, 3):
            _.append(split_col_thirds.flatten())

    groups = np.array(_)

    group_key = np.repeat(np.repeat(np.arange(9), 3).reshape(3, 9), 3, axis=0)
    """
    array([[0, 0, 0, 1, 1, 1, 2, 2, 2],
       [0, 0, 0, 1, 1, 1, 2, 2, 2],
       [0, 0, 0, 1, 1, 1, 2, 2, 2],
       [3, 3, 3, 4, 4, 4, 5, 5, 5],
       [3, 3, 3, 4, 4, 4, 5, 5, 5],
       [3, 3, 3, 4, 4, 4, 5, 5, 5],
       [6, 6, 6, 7, 7, 7, 8, 8, 8],
       [6, 6, 6, 7, 7, 7, 8, 8, 8],
       [6, 6, 6, 7, 7, 7, 8, 8, 8]])
    """

    # return set
    return {}


def driver():
    for (row, lst) in enumerate(puzzle):
        for (col, _) in enumerate(lst):
            if puzzle[row][col] is 0:
                intersection = (
                    (deck - set(puzzle[row]) - {0})
                    & (deck - set((puzzle.T)[row]) - {0})
                    & get_group_complement(row, col)
                )
                if len(intersection) is 1:
                    puzzle[row][col] = intersection


if __name__ == "__main__":
    os.system("clear")


# get specific column: [list(col) for col in zip(*p)][2]

