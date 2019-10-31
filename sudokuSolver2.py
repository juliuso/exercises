#!/usr/bin/env python
# AUTHOR: jo
# DATE: 2019-10-29
# DESCRIPTION: "Sudoku Solver" problem from codewars v2
# PROBLEM: https://www.codewars.com/kata/sudoku-solver/train
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
deck = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def get_group_complement(row, col):
    _ = []

    for split_row_thirds in np.vsplit(puzzle, 3):
        for split_col_thirds in np.hsplit(split_row_thirds, 3):
            _.append(split_col_thirds.flatten())

    groups = np.array(_)

    # Creates a key lookup table of range(9) to get the subgroup complement in _.
    group_key = np.repeat(np.repeat(np.arange(9), 3).reshape(3, 9), 3, axis=0)

    return deck - set(groups[group_key[row][col]]) - {0}


def driver():
    for (row, lst) in enumerate(puzzle):
        for (col, _) in enumerate(lst):
            if puzzle[row][col] == 0:
                intersection = (
                    (deck - set(puzzle[row]) - {0})
                    & (deck - set((puzzle.T)[col]) - {0})
                    & get_group_complement(row, col)
                )
                if len(intersection) == 1:
                    puzzle[row][col] = intersection.pop()


if __name__ == "__main__":
    while 0 in puzzle:
        driver()

    print(puzzle)

