#!/usr/bin/env python
# AUTHOR: jo
# DATE: 2019-08-12
# DESCRIPTION: Tuse homework assignment #1.

def getDistanceAndMax(matrix):

    # Initialize empty array with identical dimensions as input.
    matrix_distance = [ 
        [None for row in range(len(matrix))]
        for column in range(len(matrix[0]))
    ]

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            # Top row stays the same, and for any coordinate that's zero.
            if (row == 0) or (matrix[row][column] == 0):
                matrix_distance[row][column] = matrix[row][column]
            else:
                distance = 0

                # Iterate in reverse, from bottom to top.
                for row_range in range(row, -1, -1):
                    if matrix[row_range][column] == 1:
                        distance += 1
                    # Being explicit here to handle zero.
                    # elif can be replaced with "else: break" instead.
                    elif matrix[row_range][column] == 0:
                        break

                matrix_distance[row][column] = distance

    return {'distance' : matrix_distance,
            'max_score': max(sum(row) for row in matrix_distance)
           }

if __name__ == '__main__':
    
    snoots = [
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 1]
    ]
    
    winkler = [
        [1, 0, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]

    print(getDistanceAndMax(snoots))
    print(getDistanceAndMax(winkler))
