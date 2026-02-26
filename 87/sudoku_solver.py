# check to see if a number can be placed in a particular position
def isSafe(sudoku, row, col, num):

    # check the row
    for x in range(9):
        if sudoku[row][x] == num:
            return False

    # check the column
    for x in range(9):
        if sudoku[x][col] == num:
            return False

    # check the 3x3 square
    # define it
    startRow = row - (row % 3)
    startCol = col - (col % 3)

    # check it
    for i in range(3):
        for j in range(3):
            if sudoku[i + startRow][j + startCol] == num:
                return False

    return True

# a recursive function to check solubility of the sudoku by try out every
# possible combination (taking  sudoku restrictions into consideration)
def solveSudokuRec(sudoku, row, col):
    # if everything is filled out, we return True
    if row == 8 and col == 9:
        return True

    # if at the right edge, we go to the next row
    if col == 9:
        row += 1
        col = 0

    # if cell already occupied then go on
    if sudoku[row][col] != 0:
        return solveSudokuRec(sudoku, row, col + 1)

    # now we check and place the next number
    for num in range(1, 10):
        if isSafe(sudoku, row, col, num):
            sudoku[row][col] = num
            if solveSudokuRec(sudoku, row, col + 1):
                return True
            sudoku[row][col] = 0

    return False

def solveSudoku(sudoku):
    return solveSudokuRec(sudoku, 0, 0)


sudoku = [
    [2, 5, 1, 3, 8, 0, 7, 9, 0],
    [0, 7, 0, 1, 2, 0, 4, 3, 0],
    [0, 0, 3, 0, 6, 7, 8, 1, 0],
    [6, 2, 4, 0, 0, 3, 9, 0, 0],
    [0, 1, 0, 0, 0, 6, 0, 7, 8],
    [0, 8, 9, 2, 5, 1, 0, 4, 0],
    [0, 3, 0, 0, 0, 2, 0, 8, 9],
    [0, 9, 0, 0, 3, 0, 0, 0, 4],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    
]

print(solveSudoku(sudoku))

for row in sudoku:
        print(" ".join(map(str, row)))