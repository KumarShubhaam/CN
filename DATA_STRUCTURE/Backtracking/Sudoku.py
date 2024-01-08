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

def checkConstraints(board, row, col):
    
    if rowCheck(board, row, col) is False:
        return False
    if colCheck(board, row, col) is False:
        return False
    if boxCheck(board, row, col) is False:
        return False
    return True

def helperSudoku(board, row, col):
    if row == 9 or col == 9:
        print('----------------------------')
        for row in board:
            for i in range(len(row)):
                print(row[i], end=" ")
            print()    
        print('----------------------------')

        return True
    
    if board[row][col] != 0:
        if col == 8:
            if row == 8:
                if checkConstraints(board, row, col):
                    ans = helperSudoku(board, row+1, 0)
                else:
                    return False
            else:
                ans = helperSudoku(board, row+1, 0)
        else:
            ans = helperSudoku(board, row, col+1)
        return ans
    
    for options in range(1, 10):
        board[row][col] = options
        result = checkConstraints(board, row, col)
        if result is True:
            if col == 8:
                ans = helperSudoku(board, row+1, 0)
            else:
                ans = helperSudoku(board, row, col+1)
            if ans is True:
                return True
        
    board[row][col] = 0
    return False
    

    
    
    

    
def solveSudoku(board):
    #Implement Your Code Here
    ans = helperSudoku(board, 0, 0)
                    
    return ans








board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solveSudoku(board)
if ans is True:
    print('true')
else:
    print('false')