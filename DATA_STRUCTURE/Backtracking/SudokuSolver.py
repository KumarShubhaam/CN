def rowCheck(board, row, col):
    num = board[row][col]
    for i in range(9):
        if board[row][i] == num:
            if i != col:
                return False
    return True

def colCheck(board, row, col):
    num = board[row][col]
    for i in range(9):
        if board[i][col] == num:
            if i != row:
                return False
    return True

def boxCheck(board, row, col):
    if row <= 2:
        rowStart = 0
    elif row >= 3 and row <= 5:
        rowStart = 3
    else:
        rowStart = 6
    if col <= 2:
        colStart = 0
    elif col >= 3 and col <= 5:
        colStart = 3
    else:
        colStart = 6
    for i in range(rowStart, rowStart+3):
        for j in range(colStart, colStart+3):
            if board[i][j] == board[row][col]:
                if i != row and j != col:
                    return False
    return True

def helperSudoku(board, result, row, col):
    # if row >= 9:
    #     return result
    
    if rowCheck(board, row, col) is False:
        return False
    if colCheck(board, row, col) is False:
        return False
    if boxCheck(board, row, col) is False:
        return False


    return True

    
def solveSudoku(board):
    #Implement Your Code Here
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                ans  = helperSudoku(board, False, row, col)
                if ans is False:
                    return False
                
    return ans








board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solveSudoku(board)
if ans is True:
    print('true')
else:
    print('false')