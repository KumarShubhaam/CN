def maximumProfit(arr, i):
    
    
    if i >= len(arr):
        return -1
    
    x = arr[i]
    res = 0
    for ele in arr:
        if ele >= x:
            res = res + x
    
    
    
    i = i + 1
    price.append(maximumProfit(arr, i))
    
        
    print(price)

    return max(price)


# n = int(input())
# arr = [int(ele) for ele in input().split()]
arr = [7, 1, 2, 7, 1, 5, 6, 1, 6, 6] 
n = 10
ans = maximumProfit(arr, i=0)
print(ans)