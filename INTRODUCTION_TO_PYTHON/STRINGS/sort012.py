from sys import stdin 

def sort012(arr, n) :
    #Your code goes here
    nz = 0
    nt = n - 1
    i = 0
    while i < nt:
        if arr[i] == 0:
            arr[i], arr[nz] = arr[nz], arr[i]
            nz = nz + 1
            i = i + 1
            while arr[nz] == 0 and nz < n-1:
                nz = nz + 1
                i = i + 1
            
        elif arr[i] == 2:
            arr[i], arr[nt] = arr[nt], arr[i]
            nt = nt - 1
            
            while arr[nt] == 2 and nt >= 0:
                nt = nt - 1
            if arr[i] == 0:
                arr[i], arr[nz] = arr[nz], arr[i]
                nz = nz + 1
                i = i + 1
            
        if arr[i] == 1:
            i = i + 1
          

               






    # for i in range(n):
    #     if arr[i] == 0:
    #         arr[i], arr[nz] = arr[nz], arr[i]
    #         nz = nz + 1
    #     while arr[i] != 1 and i < nt :
    #         if arr[i] == 2 and i < nt:
    #             arr[i], arr[nt] = arr[nt], arr[i]
    #             nt = nt - 1
    #             if arr[nt] == 2:
    #                 nt = nt - 1
    #         if arr[i] == 0:
    #             arr[i], arr[nz] = arr[nz], arr[i]
    #             nz = nz + 1
























#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()

    sort012(arr, n)
    printList(arr, n)
    
    t -= 1