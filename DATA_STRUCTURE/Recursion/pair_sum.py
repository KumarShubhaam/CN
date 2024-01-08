from sys import stdin
# worng code, doesn't pass all test cases
def pairSum(arr, n, num) :
	#Your code goes here
    arr.sort()
    print(arr)
    i = 0
    j = n-1
    count = int()
    while i < j:
        
        if arr[i] + arr[j] == num:        
            a = 1
            b = 1
            
            if i < j and arr[i] == arr[i+1]:
                k = i
                while k < j and arr[k] == arr[k+1]:
                    k += 1
                a = k - i + 1
                i = k + 1
                if i < j and arr[j] == arr[j-1]:
                    k = j
                    while k > i and arr[k] == arr[k-1]:
                        k -= 1 
                    b = j - k + 1
                    j = k - 1
            else:
                i = i + 1
                j = j - 1
            print('a and b', a, b)
            count = count + a*b        
            
        elif arr[i] + arr[j] < num:
            i = i + 1
        elif arr[i] + arr[j] > num:
            j = j - 1
        
    
    return count

   

 














# arr = [1, 3, 6, 2, 5, 4, 3, 2, 4]
# arr = [3,3,3,3,3]
arr = [0,0,6,0]
n = len(arr)
print(pairSum(arr, n, 6))










# #taking input using fast I/O method
# def takeInput() :
#     n = int(stdin.readline().strip())
#     if n == 0 :
#         return list(), 0

#     arr = list(map(int, stdin.readline().strip().split(" ")))
#     return arr, n


# def printList(arr, n) : 
#     for i in range(n) :
#         print(arr[i], end = " ")
#     print()


# #main
# t = int(stdin.readline().strip())

# while t > 0 :
    
#     arr, n = takeInput()
#     num = int(stdin.readline().strip())
#     print(pairSum(arr, n, num))

#     t -= 1