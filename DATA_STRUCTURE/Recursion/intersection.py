def sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    output1 = sort(arr[0:mid])
    output2 = sort(arr[mid:len(arr)])
    newarr = list()
    i, j = 0, 0
    while i < len(output1) and j < len(output2):
        if output1[i] < output2[j]:
            newarr = newarr + [output1[i]]
            i = i + 1
        else:
            newarr = newarr + [output2[j]]
            j = j + 1
    if i < len(output1):
        while i < len(output1):
            newarr = newarr + [output1[i]]
            i = i + 1
    else:
        while j < len(output2):
            newarr = newarr + [output2[j]]
            j = j + 1
    
    return newarr
            
arr = [7, 1, 2, 7, 1, 5, 6, 1, 6, 6] 
ans = sort(arr)
print(ans)
