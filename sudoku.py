import random as random
import numpy as np

# find the empty spaces
def find(puzzle):
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                return row, column
    return None, None

# check if guess is valid (guess does not exist in the same row, column and 3 by 3 matrix)
def is_valid(puzzle, guess, row, column):
    # row_val = puzzle[row]
    # if guess in row_val:
    #     return False
    for i in range(9):
        if puzzle[row][i] == guess:
            return False

    # go through all the rows, append the value in puzzle at ith row and the col column
    # col = [puzzle[i][column] for i in range(9)]
    # if guess in col:
    #     return False
    for i in range(9):
        # if [puzzle[row][column] for row in range(9)]== guess:
        if puzzle[i][column] == guess:
            return False

    # find starting index row and column of the 3 by 3 matrix
    row_s = (row // 3) * 3  # * 3 to get the exact index
    column_s = (column // 3) * 3

    for row in range(row_s, row_s + 3):
        for column in range(column_s, column_s + 3):
            if puzzle[row][column] == guess:
                return False
    return True

# use backtracking and recursion
def solve(puzzle):
    # attempt on the empty space found
    row, column = find(puzzle)

    # if row or column is None, puzzle is solved
    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, column):
            # guess a number
            puzzle[row][column] = guess
            if solve(puzzle):
                return True
        # if guess is invalid/ does not solve the puzzle, backtrack and attempt again
        puzzle[row][column] = 0 # reset value

    # if all guesses attempted and still doesn't work
    return False

if __name__ == '__main__':
    example = [
        [3, 9, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 5],
        [0, 0, 0, 7, 1, 9, 0, 8, 0],

        [0, 5, 0, 0, 6, 8, 0, 0, 0],
        [2, 0, 6, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],

        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 7, 0, 0, 0, 5, 0, 4, 0],
        [1, 0, 9, 0, 0, 0, 2, 0, 0]
    ]
    print(solve(example))
    print(example)
