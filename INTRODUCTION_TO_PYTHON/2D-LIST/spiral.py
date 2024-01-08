from sys import stdin

def spiralPrint(mat, nRows, mCols):
     #Your code goes here
    rs = 0
    cs = 0
    re = nRows-1
    ce = mCols-1
    k = 0
    while k < nRows*mCols:
        # LOOP FOR 1ST TRAVERSAL
        if k >= nRows*mCols:
                break
        for i in range(cs, ce+1):
            print(mat[rs][i], end=" ")
            k = k + 1
        rs = rs + 1
        
        # LOOP FOR 2nd TRAVERSAL
        if k >= nRows*mCols:
                break
        for i in range(rs, re+1):
            print(mat[i][ce], end=" ")
            k = k + 1
        ce = ce - 1
        
        # LOOP FOR 3rd TRAVERSAL
        if k >= nRows*mCols:
                break
        for i in range(ce, cs-1, -1):
            print(mat[re][i], end=" ")
            k = k + 1
        re = re - 1
        
        # LOOP FOR 4th TRAVERSAL
        if k >= nRows*mCols:
                break
        for i in range(re, rs-1 , -1):
            print(mat[i][cs], end=" ")
            k = k + 1
            if k > nRows*mCols:
                break
        cs = cs + 1
        
mat = [[1,2,3,4], 
       [5,6,7,8], 
       [9, 10, 11,12]]
nRows = 3
mCols = 4
spiralPrint(mat, nRows, mCols)
        
        
        




























'''

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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
    
    '''