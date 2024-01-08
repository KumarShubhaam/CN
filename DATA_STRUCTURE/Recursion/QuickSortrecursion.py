from typing import List

def quickSort(arr: List[int], startIndex: int, endIndex: int):
    pass
    
    if startIndex >= endIndex:
        return
    i = partition(arr, startIndex, endIndex)
    quickSort(arr, startIndex, i-1)
    quickSort(arr, i+1 , endIndex)


def partition(arr, startIndex, endIndex):
    p = startIndex
    count = 0

    for i in range(startIndex+1, endIndex +1):
        if arr[i] < arr[p]:
            count += 1        
    # arr[count + startIndex], arr[p] = arr[p], arr[count + startIndex]
    arr[count + startIndex], arr[startIndex] = arr[startIndex], arr[count + startIndex]
    p = startIndex+count
    i = startIndex
    j = endIndex
    # print('p here', p)
    
    # print(arr, 'here')
    while i < p and j > p:
        # print(arr[i], arr[p], arr[j])
        if arr[i] >= arr[p] and arr[j] <= arr[p]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] < arr[p]:
            i += 1
        else:
            j -= 1
    return p


arr = [9,9,7,7,5,4,4]

print('arr = ', arr)
quickSort(arr, 0, len(arr)-1)
part = partition(arr, 0, len(arr)-1)
# print(arr)
print(" ".join(str(x) for x in arr))
# print(arr[part])