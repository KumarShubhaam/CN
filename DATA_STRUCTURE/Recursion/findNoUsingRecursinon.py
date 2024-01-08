def checkNumber(arr, x):
    # Please add your code here
    pass
    n = len(arr)
    # print(n)
    # print("arr[0]", arr[0])
    if arr[0] == x:
        # print(arr[0], "this line got executed")
        return True
    elif arr[0] != 0 and n > 1:
        # print(arr[1: n])
        return checkNumber(arr[1: n], x)
    else:
        return False






















# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
