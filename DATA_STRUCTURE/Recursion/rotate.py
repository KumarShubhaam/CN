def rotate(arr, n, x):
    #Your code goes here
    arr.reverse()
    print(arr)
    arr[0:n-x] = list(reversed(arr[0:n-x]))
    arr[n-x:] = list(reversed(arr[n-x:] ))
    return arr


    



n = 7
arr = [1, 2, 3, 4, 5, 6, 7]
print(rotate(arr, n, 2))

