'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin

def findLargest(arr, nRows, mCols):
    #Your code goes here
    
    row_max = 0
    col_max = 0
    row_index = -1
    col_index = -1
    for i in range(nRows):
        r_sum = 0
        for j in range(mCols):
            r_sum += arr[i][j]         # ROW SUM GOES HERE
           
        if r_sum > row_max:
            row_max = r_sum
            row_index = i
    
                                     # COL SUM GOES HERE
    for i in range(mCols):
        c_sum = 0
        for j in range(nRows):
            c_sum += arr[j][i]         

        if c_sum > col_max:
            col_max = c_sum
            col_index = i
    
    
    if row_max > col_max:
        print("row" + " " + str(row_index) + " " + str(row_max))
    elif col_max > row_max:
        print("column" + " " + str(col_index) + " " + str(col_max))
    else:
        print("row" + " " + str(row_index) + " " + str(row_max))



    

























#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1