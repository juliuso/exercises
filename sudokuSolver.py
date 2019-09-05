#!/usr/bin/env python
# AUTHOR: jo
# DATE: 2019-08-28
# DESCRIPTION: "Sudoku Solver" problem from codewars
# PROBLEM: https://www.codewars.com/kata/sudoku-solver/train/


#[0][0:3] [3:6] [6:9]
#[1:3] 


puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

horizontal = [ [None for row in range(len(puzzle))]
                for column in range(len(puzzle))
            ]

vertical = [ [None for row in range(len(puzzle))]
                for column in range(len(puzzle))
            ]

def getOptions(line) -> 'List of possible choices.':
    # line refers to going across, down, or within the 3x3 grid
    # line: [5,3,0,0,7,0,0,0,0]
    masterDeck = [1,2,3,4,5,6,7,8,9]
    updatedDeck = []

    for el in range(len(line)):
        if line[el] in masterDeck:
            masterDeck.remove(line[el])
        

    return lstDeck

def across():
    for row in range(len(puzzle)):
        for el in range(len(puzzle[row])):
            if (puzzle[row][el] == 0):
                puzzle[row][el] = getOptions(puzzle[row])
            if (type(puzzle[row][el]) != int):
                puzzle[row][el] = getOptions(puzzle[row])
                

def within():
    pass

def down():
    pass

if __name__ == '__main__':
    print('Awesome!')

    across()
    print(puzzle[0])