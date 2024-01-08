from os import *
from sys import *
from collections import *
from math import *

def printarray(arr, n, m):
    for i in range(n, 0, -1):
        for j in range(i):
            print(" ".join(str(ele) for ele in arr[n - i]))

n, m = [int(x) for x in input().split()]
# print(n, m)
# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = [[int(j) for j in input().split()] for i in range(n)]
# print(arr)
printarray(arr, n, m)