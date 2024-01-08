def firstIndex(arr, x, si=0):
    # Please add your code here
    pass
    if arr[si] == x and si < len(arr)-1:
        return si
    elif arr[si] != x and si < len(arr)-1:
        return firstIndex(arr, x, si+1)
    
    return -1




















# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))
