import Print 

def Print(maze):
    print('----------------------------')
    for row in maze:
        for i in range(len(row)):
            print(row[i], end=" ")
        print()   
    print('----------------------------')


def NQueen(n, board, x, y, count):
    if n == 0:
        return
    # if x >= n :
    #     Print(board)
    #     return
        
    if x < 0 or y < 0 or x >= n or y >= n or board[x][y] == 1:
        return
    
    # Column check
    for i in range(0, n):
        if board[x][i] == 1:
            return
        
    # Row check
    for i in range(0, n):
        if board[i][y] == 1:
            return
        
    #Left to Right Diagnol check upward
    i = x
    j = y
    while (i >=0) and (j >= 0):
        try:
            if board[i][j] == 1:
                return
            i = i - 1
            j = j - 1
        except:
            print(i , j)
    #Downward
    i = x
    j = y
    while (i < n) and (j < n):
        if board[i][j] == 1:
            return
        i = i + 1
        j = j + 1

    #Right to Left Diagnol check upward
    j = x
    i = y
    while (i < n) and (j >= 0):
        if board[j][i] == 1:
            return 
        j = j - 1 
        i = i + 1
    # Downward
    j = x
    i = y
    while (i >= 0) and (j < n):
        if board[j][i] == 1:
            return
        j = j + 1
        i = i - 1
    
    board[x][y] = 1
    if board[x][y] == 1:
        count = count + 1
        for j in range(n):
            NQueen(n, board, x+1, j, count)
        

    if count == n:
        Print(board)
    board[x][y] = 0
    return
        
    

n = input("enter N: ")
n = int(n)
count = 0
board = [[0 for j in range(n)] for x in range(n)]
for k in range(n):
    NQueen(n, board, 0, k, count)
