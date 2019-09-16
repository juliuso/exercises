#!/usr/bin/env python
# AUTHOR: jo
# DATE: 2019-09-15
# DESCRIPTION: "Sudoku Solver" problem from codewars
# PROBLEM: https://www.codewars.com/kata/sudoku-solver/train
from os import system
from time import sleep

puzzle = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

# Print puzzle as it mutates.
def printPuzzle():
    print('=' * 80)
    for row in range(len(puzzle)):
        print(f'r{row}: {puzzle[row]}')

# Each zero replaced with [ set(), set(), set() ]
# list_[0] is the set complement of numbers going across each row.
# list_[1] is the set complement of numbers going down each column.
# list_[2] is the set complement of numbers within each respective 3x3 group.
def initializePuzzle():
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] is 0:
                puzzle[row][col] = [set(), set(), set()]

# Returns the sudoku set complement of any list passed into it.
# Input:  [2, 4, 6]
# Output: {1, 3, 5, 7, 8, 9}
def complement(lst):
    _deck = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for el in lst:
        if (type(el) is int) and (el in _deck):
            _deck.remove(el)
    return _deck

# While loop in main keeps running until all lists in puzzle
# are replaced with integers.
def puzzleFinished() -> 'Boolean checks if puzzle is complete (no list exist)':
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if type(puzzle[row][col]) is list:
                return False
    return True

# After each epoch of complements, the row, column, and group complements
# are intersected. If the intersection returns exactly 1 element, then
# replace the list of sets with that element.
def intersect():
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if type(puzzle[row][col]) is list:
                if len(puzzle[row][col][0]
                    & puzzle[row][col][1]
                    & puzzle[row][col][2]) is 1:
                    _commonElement = (puzzle[row][col][0]
                                        & puzzle[row][col][1]
                                        & puzzle[row][col][2]).pop()
                    print(f'+++++Set intersection yields 1 element at ({row}, {col}). ' \
                            f'Replacing set with {_commonElement}.+++++')
                    puzzle[row][col] = _commonElement

# Step 1: Process each row and assign unknown values
# the set complement of the row.
def rows():
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if type(puzzle[row][col]) is list:
                puzzle[row][col][0] = complement(puzzle[row])

# Step 2: Process each column and assign unknown values
# the set complement of the column.
def columns():
    columns_ = [ [row[col] for row in puzzle] for col in range(len(puzzle)) ]
    choices_ = []
    
    for row in columns_:
        choices_.append(complement(row))

    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if type(puzzle[row][col]) is list:
                puzzle[row][col][1] = choices_[col]

# Step 3: Process each 3x3 group and assign unknown values
# the set complement of the group.
def group():
    # Group number of each 3x3 group in puzzle corresponds
    # to the row number in groups_. 
    # 0 | 1 | 2
    # ----------
    # 3 | 4 | 5 
    # ----------
    # 6 | 7 | 8

    # Bundle each group into a list.
    groups_ = [
        [ puzzle[0][0:3] + puzzle[1][0:3] + puzzle[2][0:3] ],
        [ puzzle[0][3:6] + puzzle[1][3:6] + puzzle[2][3:6] ],
        [ puzzle[0][6:9] + puzzle[1][6:9] + puzzle[2][6:9] ],
        [ puzzle[3][0:3] + puzzle[4][0:3] + puzzle[5][0:3] ],
        [ puzzle[3][3:6] + puzzle[4][3:6] + puzzle[5][3:6] ],
        [ puzzle[3][6:9] + puzzle[4][6:9] + puzzle[5][6:9] ],
        [ puzzle[6][0:3] + puzzle[7][0:3] + puzzle[8][0:3] ],
        [ puzzle[6][3:6] + puzzle[7][3:6] + puzzle[8][3:6] ],
        [ puzzle[6][6:9] + puzzle[7][6:9] + puzzle[8][6:9] ],
    ]
    
    # Holds the complement of groups_.
    choices_ = []

    # Scans through each group, bundle the ints together,
    # and get its complement.
    for grp in groups_:
        bundle_ = []

        for el in grp:
            for subEl in el:
                if type(subEl) is int:
                    bundle_.append(subEl)

        choices_.append(complement(bundle_))

    # Assign the group complement based on the
    # coordinate of each puzzle piece.
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if type(puzzle[row][col]) is list:
                if 0 <= row <= 2:
                    if 0 <= col <= 2:
                        puzzle[row][col][2] = choices_[0]
                    if 3 <= col <= 5:
                        puzzle[row][col][2] = choices_[1]
                    if 6 <= col <= 8:
                        puzzle[row][col][2] = choices_[2]
                if 3 <= row <= 5:
                    if 0 <= col <= 2:
                        puzzle[row][col][2] = choices_[3]
                    if 3 <= col <= 5:
                        puzzle[row][col][2] = choices_[4]
                    if 6 <= col <= 8:
                        puzzle[row][col][2] = choices_[5]
                if 6 <= row <= 8:
                    if 0 <= col <= 2:
                        puzzle[row][col][2] = choices_[6]
                    if 3 <= col <= 5:
                        puzzle[row][col][2] = choices_[7]
                    if 6 <= col <= 8:
                        puzzle[row][col][2] = choices_[8]

# Will be called continuously until the puzzle's solved.
# Each cycle ends with a 1 second delay to observe the change
# in the puzzle's state.
def cycle():
    system('clear')
    rows()
    columns()
    group()
    intersect()
    printPuzzle()
    sleep(1)

if __name__ == '__main__':
    initializePuzzle()

    while not puzzleFinished():
        cycle()