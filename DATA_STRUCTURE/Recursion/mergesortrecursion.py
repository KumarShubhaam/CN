def mergeSort(arr: [int], l: int, r: int):
    # Write Your Code Here
    pass
    n = len(arr)
    mid = n//2
    if n == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
            return arr
        else:
            return arr
    elif n < 2:
        return arr
    s1 = arr[0:mid]
    s2 = arr[mid:]
    # print('s1', s1, 's2', s2)
    output1 = mergeSort(s1, 0, mid-1)
    # print('output1', output1)
    output2 = mergeSort(s2, mid, n-1)
    # print('output2', output2)
    # i = 0
    j, k = 0,0
    newarr = []
    while j < len(output1) and k < len(output2):
        # print(s1[j], '<', s2[k] )
        if output1[j] < output2[k]:
            newarr.append(output1[j])
            # print('s1[j]', s1[j])
            j = j + 1
        else:
            newarr.append(output2[k])
            k = k + 1
        # i = i + 1
    # print('after 1st loop', newarr)
    while j < len(output1):
        newarr.append(output1[j])
        j = j + 1
        # i = i + 1
    while k < len(output2):
        newarr.append(output2[k])
        k = k + 1
        # i = i + 1
    
    for i in range(len(newarr)):
        arr[i] = newarr[i]
    return newarr
    

    











# n = int(input())
n = 5
# arr = [int(x) for x in input().split()]
arr = [9, 3, 6, 2, 0]
mergeSort(arr, 0, len(arr)-1)
print(arr)